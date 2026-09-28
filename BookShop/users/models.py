from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13, blank=True)
    birth_date = models.DateField(blank=True, null=True)