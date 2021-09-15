from django.db import models


# Create your models here.
class Emloyee(models.Model):
    emp_id = models.CharField(primary_key=True, max_length=200)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
