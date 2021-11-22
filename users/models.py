from django.db import models
# from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager

# Create your models here.

class UserManager(UserManager):
   
   def create_user(self, username, email="", password=None,   #endret noen felt til "" til tom streng
         age = None, address = "", allergies="", city = ""):

      user = self.model(username = username,
                        email = email,
                        password = password,
                        age = age,
                        address = address,
                        allergies = allergies,
                        city = city)
      
      user.set_password(password)
      user.save(using=self._db)
      return user

   def create_superuser(self, username, email="", password=None,
         age = None, address = "", allergies = "", city = ""):
      user = self.model(username = username,
               email = email,
               password = password,
               age = age,
               address = address,
               allergies = allergies,
               city = city
               )
      user.set_password(password)
      user.is_admin = True
      user.is_moderator = True
      user.save(using=self._db)
      return user

class OwnUser(models.Model):
   username = models.CharField(max_length=50, default=None)
   password = models.CharField(max_length=50, default=None)
   name = models.CharField(max_length=50, default=None)
   age = models.IntegerField(default=None)
   address = models.CharField(max_length=50, default=None)
   allergies = models.TextField(default=None)
   city = models.CharField(max_length=50, default="")
   #gender = models.CharField(widget=forms.Select(choices=GENDER_CHOICES))

class User(AbstractUser):
   # name = models.CharField(max_length=50, default=None)
   age = models.IntegerField(default=True)
   address = models.CharField(max_length=50, blank=True)
   allergies = models.TextField(blank=True)
   city = models.CharField(max_length=50, default="")

   is_admin = models.BooleanField(default=False)