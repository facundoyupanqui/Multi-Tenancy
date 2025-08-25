from django.db import models
from clients.models import Client

class Product(models.Model):
    client = models.ForeignKey(
        Client, 
        on_delete=models.CASCADE, 
        related_name="products",
        null=True,      # permite que sea vacío temporalmente
        blank=True      # permite que el formulario del admin lo deje vacío
    )
    name = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.name} ({self.client.name})" if self.client else self.name
