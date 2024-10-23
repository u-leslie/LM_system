from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.delivery_create, name='delivery_create'),
    path('', views.deliveries_list, name='deliveries_list'),
    path('<str:delivery_id>/', views.delivery_detail, name='delivery_detail'),
]
