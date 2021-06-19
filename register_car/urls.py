from register_car.models import RegisterCar
from django.urls import path

from register_car.views import RegisterCar


urlpatterns = [
    path("registercar/", RegisterCar.as_view(), name="registercar"),
    path("registercar/<action>", RegisterCar.as_view(), name="registercar"),
    path("registercar/<action>/<id>", RegisterCar.as_view(), name="registercar"),
]