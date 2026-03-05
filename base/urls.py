from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('products/', views.getProducts, name='products'),
    path('products/<str:pk>/', views.getProduct, name='product'),
    path('conversations/', include('conversations.urls')),
    path('auth/', include('authentication.urls')),
]
