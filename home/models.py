from django.db import models

# Create your models here.
#example we have a student schema
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    parent_name = models.CharField(max_length=50)
    address = models.TextField()
    assignment = models.FileField()
    