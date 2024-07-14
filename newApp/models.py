from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=30)
    roll_number=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()


