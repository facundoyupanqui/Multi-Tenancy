from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    client = models.ForeignKey('clients.Client', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.username} ({self.client})" if self.client else self.username
