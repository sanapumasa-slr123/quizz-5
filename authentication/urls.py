from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register_view, name='register'),
    path('signin/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
