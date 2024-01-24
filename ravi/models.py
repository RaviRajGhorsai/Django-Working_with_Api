from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 100)
    roll_number = models.IntegerField()
    age = models.IntegerField()
    address = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.name}"

class Teacher(models.Model):
    name = models.CharField(max_length = 50)
    subject = models.CharField(max_length = 50)
    phone = models.CharField(max_length= 10)
    address = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.name}"