from django.db import models
class Person(models.Model):
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    nationalCode = models.CharField(max_length=10)

