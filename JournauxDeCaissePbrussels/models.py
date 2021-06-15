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
    plate = models.CharField(max_length=8)

class Amonds(models.Model):
    recipe_fk = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='recipe_fk')
    payement_fk = models.ForeignKey('Payment', on_delete=models.CASCADE,related_name='payement_fk')
    employee_fk = models.ForeignKey('Employee', on_delete=models.CASCADE,related_name='employee_fk')
