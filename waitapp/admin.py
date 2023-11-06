from django.contrib import admin
from .models import TruckDriver

# Register your models here.
@admin.register(TruckDriver)
class TruckDriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'truck_number', 'company', 'check_in', 'status', 'in_progress_time', 'finished_time')
    list_filter = ('name', 'truck_number', 'company')
    search_fields = ('name', 'truck_number', 'company')
