import uuid

from django.db import models


class VerificationPhoneNumber(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=15)
    key = models.CharField(max_length=7)
    verify = models.BooleanField(default=False)
    code = models.CharField(max_length=6)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, null=True)
