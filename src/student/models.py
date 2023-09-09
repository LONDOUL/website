from django.db import models
from django.http import JsonResponse


class Student(models.Model):
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)


