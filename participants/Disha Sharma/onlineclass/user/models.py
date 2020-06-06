from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField

import datetime
YEAR_CHOICES = []
for r in range(1984, (datetime.datetime.now().year+5)):
    YEAR_CHOICES.append((r,r))

APPROVAL_CHOICES = (
    ('hindi', 'Hindi'),
    ('english', 'English'),
    ('french', 'French'),
    )

class Subject(models.Model):
    name = models.CharField(max_length=30,blank=False,default=False)
    
    def __str__(self):
        return self.name

#Sang@niit11
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    courses = models.ForeignKey(Subject, on_delete=models.CASCADE,default=1)
    first_name = models.CharField(max_length=30,blank=False,default=False)
    last_name = models.CharField(max_length=30,blank=True,default=False)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    college= models.CharField(max_length=120,blank=False,default=False)
    degree = models.CharField(max_length=30,blank=False,default=False)
    major = models.CharField(max_length=60,blank=False,default=False)
    year = models.IntegerField(choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    image = models.ImageField(upload_to='images/')
    LinkedIn = models.URLField(default='null')
    lang_approved = models.CharField(max_length=10,choices=APPROVAL_CHOICES)