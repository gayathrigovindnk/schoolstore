from datetime import date
from django.forms.widgets import SelectDateWidget  # Correct

from django.contrib.admin import widgets
from django.db import models
from django import forms

from numpy.ma import extras


# Create your models here.
class department(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class course(models.Model):
    department=models.ForeignKey(department, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name


class purpose(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name


class material(models.Model):
    name=models.CharField(max_length=50)


    def __str__(self):
        return self.name

class student(models.Model):
    gender_choices=[
        ("m","male"),
        ("f","female")
    ]
    name=models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.IntegerField()
    birth_date = models.DateField()
    mailid = models.EmailField()
    address= models.CharField(max_length=50)
    gender=models.CharField(max_length=1,choices=gender_choices,default="m")
    department = models.ForeignKey(department,on_delete=models.SET_NULL,blank=True, null=True)
    course = models.ForeignKey(course,on_delete=models.SET_NULL,blank=True, null=True)
    purpose = models.ForeignKey(purpose,on_delete=models.SET_NULL,blank=True, null=True)
    material = models.ForeignKey(material,on_delete=models.SET_NULL,blank=True, null=True)
    def __str__(self):
        return self.name

