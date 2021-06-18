from django.db import models

class RegisterCar(models.Model):

    name = models.CharField(max_length=20)
    type_car = models.CharField(max_length=20)
    plaque = models.CharField(max_length=8)
    value = models.FloatField()


    def __str__(self) -> str:
        return f'{self.name} - {self.type_car} - {self.plaque} - {self.value}'
