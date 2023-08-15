from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import UserManager

from .manager import CustomUserManager



class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, blank=False, null=True, unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        return self.username
    
    USERNAME_FIELD = 'username'

    
    objects = CustomUserManager()
