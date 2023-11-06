from .models import TruckDriver
from django import forms

class TruckDriverForm(forms.ModelForm):
    class Meta:
        model = TruckDriver
        fields = ['name', 'truck_number', 'company']
    name = forms.CharField(label='Driver Name', max_length=200)
    truck_number = forms.CharField(label='Truck Number', max_length=200)
    company = forms.CharField(label='Company', max_length=200)
    

