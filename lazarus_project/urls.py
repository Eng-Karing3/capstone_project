"""
URL configuration for lazarus_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.http import JsonResponse
from . import views

def home(request):
    return JsonResponse({
        "message": "🚀 Welcome to Lazarus Project API",
        "description": "An upcycling and sustainable fashion backend service.",
        "available_endpoints": {
            "Admin": "/admin/",
            "Accounts": "/accounts/",
            "Users": "/users/",
            "Products": "/products/",
            "Orders": "/orders/",
            "Leads": "/leads/",
            "Auth Token": "/api/token/",
            "Refresh Token": "/api/token/refresh/"
        },
        "status": "Running smoothly ✅"
    })


urlpatterns = [
    
    path("", views.home, name="home"), 
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('users/', include('users.urls')),
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
    path('leads/', include('leads.urls')),

    # ✅ JWT endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]







