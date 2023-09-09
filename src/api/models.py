from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100)
    rotation_period = models.CharField(max_length=10)
    orbital_period = models.CharField(max_length=10)
    diameter = models.CharField(max_length=10)
    climate = models.CharField(max_length=100)
    gravity = models.CharField(max_length=100)
    terrain = models.CharField(max_length=100)
    surface_water = models.CharField(max_length=10)
    population = models.CharField(max_length=20)

    def __str__(self):
        return self.name


