from django.db import models

from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'username'
    username=models.CharField(max_length=150,unique=False)
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('utilisateur', 'Utilisateur'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='utilisateur')
    # USERNAME_FIELD = 'email'