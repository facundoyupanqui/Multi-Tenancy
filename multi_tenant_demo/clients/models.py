from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100, unique=True)
    domain = models.CharField(max_length=100, unique=True)  # agregado
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
