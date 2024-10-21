

from django.urls import path
from . import views

urlpatterns = [
    path('', views.shipment_list, name='shipments_list'),
    path('<int:pk>/', views.shipment_detail, name='shipment_detail'),
    path('create/', views.shipment_create, name='shipments_form'),
    path('edit/<int:pk>/', views.shipment_edit, name='shipment_edit'),
    path('delete/<int:pk>/', views.shipment_delete, name='shipment_delete'),
]
