from car.models import carmodel
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = carmodel
        fields = ['car_model', 'car_owner','car_color','car_number','description','service_type','submission_date','year_old','servicing']

