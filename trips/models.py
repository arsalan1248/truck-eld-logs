from django.db import models
from common.model_utils import BaseModel


# Create your models here.
class Trip(BaseModel):
    current_location = models.CharField(max_length=255)
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    current_cycle_used = models.FloatField()

    def __str__(self):
        return f"Trip from {self.pickup_location} to {self.dropoff_location}"
    

class LogSheet(BaseModel):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='logs')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    driving_hours = models.FloatField()
    rest_hours = models.FloatField()

    def __str__(self):
        return f"Log for {self.date}"