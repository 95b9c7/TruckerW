from django.db import models

# Create your models here.
class TruckDriver(models.Model):
    name = models.CharField(max_length=200, default='-')
    truck_number = models.CharField(max_length=200, default='-')
    company = models.CharField(max_length=200, default='-')
    check_in = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, default='Waiting')
    in_progress_time = models.DateTimeField(null=True, blank=True)
    finished_time = models.DateTimeField(null=True, blank=True)