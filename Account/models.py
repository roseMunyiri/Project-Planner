from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, blank=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'username']
    
    

