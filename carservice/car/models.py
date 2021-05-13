from django.db import models
from django.urls import  reverse


class carmodel(models.Model):
    SEVICECHOICES = [('PLATINUM','PLATINUM'),('GOLD','GOLD')]
    SERVICE = [('Full-vehicle inspection and correction of any issues','Full-vehicle inspection and correction of any issues'),
               ('Repack wheel bearings','Repack wheel bearings'),('Suspension check','Suspension check'),('Windscreen wiper replacement','Windscreen wiper replacement'),
               ('Wheel alignment','Wheel alignment'),('Transmission service','Transmission service'),('Coolant flush','Coolant flush'),('Brake fluid and brakes check','Brake fluid and brakes check'),
               ('Air-conditioner filter check','Air-conditioner filter check'),('Spark plug replacement','Spark plug replacement'),('Lights check','Lights check'),
               ('Engine check','Engine check')]
    car_model = models.CharField(max_length=100)
    car_owner = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)
    car_number = models.CharField(max_length=30)
    description = models.TextField()
    service_type = models.CharField(choices=SEVICECHOICES,blank=True, max_length=8)
    submission_date = models.DateTimeField()
    year_old = models.IntegerField(null=True)
    servicing = models.CharField(choices=SERVICE, blank=True, max_length=100)


    class Meta:
        verbose_name = 'carmodel'
        verbose_name_plural = 'carmodel'

    def get_absolute_url(self):
        return reverse('list')
