from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=100)
    phone_number = models.CharField(unique=True, max_length=15)

    USERNAME_FIELD = "email"
