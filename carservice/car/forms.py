from django import forms
from car.models import carmodel


class carform(forms.ModelForm):
    class Meta:
        model = carmodel
        fields = '__all__'