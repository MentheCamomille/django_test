from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import ATokenObtainPairSerializer, UserSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Product
from .forms import ProductForm, RegisterForm, LoginForm
from django.contrib.auth.models import User

class Topv(TokenObtainPairView):
    serializer_class = ATokenObtainPairSerializer

class TokenRefreshView(TokenRefreshView):
    pass

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            new_user = User.objects.create_user(username=username, password=password)
            new_user.save()
            return redirect('login') 
    else:
        form = RegisterForm()
    return render(request, 'authentication/register.html', {'form': form})

def registration_success(request):
    return render(request, 'authentication/register_success.html')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})

def dashboard(request):
    return render(request, 'authentication/dashboard.html')

def admin_products(request):
    products = Product.objects.all()
    product_list = "\n".join([f"{product.name} - {product.price} - {product.description}" for product in products])
    return HttpResponse(product_list)

def admin_products_html(request):
    products = Product.objects.all()
    return render(request, 'authentication/admin_products.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            price = form.cleaned_data['price']
            description = form.cleaned_data['description']
            product = Product(name=name, price=price, description=description)
            product.save()
            return redirect('admin_products')
    else:
        form = ProductForm()
    return render(request, 'authentication/add_product.html', {'form': form})
