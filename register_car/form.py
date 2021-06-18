from django import forms
from django.forms import ModelForm

from register_car.models import RegisterCar


class RegisterCarForms(ModelForm):
    class Meta:
        model = RegisterCar
        fields = '__all__'