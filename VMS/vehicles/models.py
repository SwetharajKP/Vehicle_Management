from django.db import models

# Create your models here.

class Vehicle(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=50)
    mileage = models.FloatField()

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"