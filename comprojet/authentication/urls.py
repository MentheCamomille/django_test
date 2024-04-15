from django.urls import path
from .views import Topv, TokenRefreshView, RegisterUser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from django.urls import path
from .views import add_product, admin_products, admin_products_html
from .views import register, login, dashboard


urlpatterns = [
    path('token/', Topv.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('products/add/', add_product, name='add_product'),
    path('admin/products/', admin_products, name='admin_products'),
    path('admin/products/html/', admin_products_html, name='admin_products_html'),
]

class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    