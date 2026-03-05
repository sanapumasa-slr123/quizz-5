from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_view, name='chat'),
    path('list/', views.conversation_list_view, name='conversation_list'),
    path('<int:pk>/', views.conversation_detail_view, name='conversation_detail'),
]
