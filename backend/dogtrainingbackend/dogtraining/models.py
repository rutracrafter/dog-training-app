from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Dog(models.Model):
    photo = models.ImageField(upload_to="images/", blank=True)
    name = models.CharField(max_length=30, blank=False)
    age = models.PositiveSmallIntegerField(default=1, validators=[MaxValueValidator(100)], blank=True)
    food = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(100)], blank=True)
    progress = models.JSONField(blank=True)
    creation_date = models.DateTimeField(default=datetime.now)
    owners = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return f"{self.name}"