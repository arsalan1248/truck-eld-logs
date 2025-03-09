import uuid
from django.db import models
from django.contrib import admin


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)
    list_per_page = 20
    # formfield_overrides = {
    #     JSONField: {"widget": JSONEditorWidget},
    # }


class BaseAdminWithAudit(BaseAdmin):
    base_fields = (
        "created_at",
        "updated_at",
    )

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        fieldsets[0][1]["fields"] = [
            field
            for field in fieldsets[0][1]["fields"]
            if field not in self.base_fields
        ]
        if not isinstance(fieldsets, list):
            fieldsets = list(fieldsets)
        fieldsets.append(
            (
                "Additional Information",
                {"fields": self.base_fields, "classes": ["collapse"]},
            )
        )

        return fieldsets

    def get_list_filter(self, request):
        list_filters = super().get_list_filter(request)
        return set(list_filters) | set(self.base_list_filters)

    # def has_delete_permission(self, request, obj=None):
    #     return not DISABLE_DELETE