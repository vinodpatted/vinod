from django.contrib import admin
from car.models import carmodel

class caradmin(admin.ModelAdmin):
    list_display = ['id','car_model','car_owner','car_color','car_number','description',]


admin.site.register(carmodel,caradmin)
