from django.db import models
from .user import User


class FoodConfigParam(models.Model):
    name = models.CharField(max_length=100)
    percent = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)