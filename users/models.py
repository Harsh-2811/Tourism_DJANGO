from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=120,unique=True)
    username = models.CharField(max_length=120,unique=True)
    first_name = models.CharField(max_length=100,default=" ")
    last_name = models.CharField(max_length=100,default=" ")
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email