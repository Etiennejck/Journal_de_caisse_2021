from django.db import models
from django.contrib.auth.models import User


class Employee(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    function = models.CharField(max_length=100)

class Recipe(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=100)
    amonds = models.DecimalField(max_digits=10,decimal_places=2)
    communications = models.TextField()

class Payment(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=100)
    amonds = models.DecimalField(max_digits=10, decimal_places=2)
    plate = models.charField(max_length=8)

class Amonds(models.Model):
    recipeFK = models.ForeignKey('Recipe', on_delete=models.CASCADE,)
    payementFK = models.ForeignKey('Payment', on_delete=models.CASCADE,)
    employeeFK = models.ForeignKey('Employee', on_delete=models.CASCADE,)
