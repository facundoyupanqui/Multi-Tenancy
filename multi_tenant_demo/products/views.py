from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Product
from clients.models import Client

@login_required
def product_list(request):
    try:
        client = Client.objects.get(customuser=request.user)
        products = Product.objects.filter(client=client)
    except Client.DoesNotExist:
        products = []
    return render(request, 'product_list.html', {'products': products})
