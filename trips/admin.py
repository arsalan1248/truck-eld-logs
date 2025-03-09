from django.contrib import admin
from trips import models
from common.model_utils import BaseAdminWithAudit

# Register your models here.
@admin.register(models.Trip)
class TripAdmin(BaseAdminWithAudit):
    list_display = (
        "id",
        "current_location",
        "pickup_location",
        "dropoff_location",
    )


@admin.register(models.LogSheet)
class LogSheetAdmin(BaseAdminWithAudit):
    list_display = (
        "id",
        "date",
        "start_time",
        "end_time",
    )