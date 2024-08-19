from django.db import models
from application.models import Application

# Create your models here.
class Employer(models.Model):
    name = models.CharField(max_length=30)
