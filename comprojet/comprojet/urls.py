"""comprojet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from authentication import views
from django.urls import path, include
from django.http import HttpResponse
from authentication.views import register, user_login

def home(request):
    return HttpResponse("Hello World !")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('registration-success/', views.registration_success, name='registration_success'),
    path('', home), 
]   