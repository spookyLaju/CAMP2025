from django.db import models

# Create your models here.
from django.db import models
import uuid

class Event(models.Model):
    image = models.ImageField(upload_to='events/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date  = models.DateTimeField()
    location = models.CharField(max_length=255)
  

    def __str__(self):
        return self.name
    



class Youth(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, primary_key=True)
    date_of_birth = models.DateField()
    branch = models.CharField(max_length=100, null=False)
    district = models.CharField(max_length=20, null=False)
    department = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)