from django.contrib import admin
from .models import CarMake, CarModel

# Register the CarMake and CarModel models
admin.site.register(CarMake)
admin.site.register(CarModel)