from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Dog(models.Model):
    photo = models.ImageField(upload_to="./images/")
    name = models.CharField(max_length=30)
    food = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)])
    progress = models.JSONField()