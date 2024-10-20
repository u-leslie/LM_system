from django.urls import path
from . import views

urlpatterns = [
    path('', views.delivery_list, name='delivery_list'),
    path('<int:pk>/', views.delivery_detail, name='delivery_detail'),
]
