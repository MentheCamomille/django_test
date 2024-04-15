from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def admin_products(request):
    products = Product.all()
    product_list = "\n".join([f"{product.name} - {product.price} - {product.description}" for product in products])
    return HttpResponse(product_list)

def admin_products_html(request):
    products = Product.all()
    return render(request, 'admin_products.html', {'products': products})