from django.urls import path
from . import views

urlpatterns = [
    path('shipments/', views.shipments_list, name='shipments_list'),
    path('shipments/<uuid:shipment_id>/', views.shipment_detail, name='shipment_detail'),
    path('create/', views.shipment_create, name='shipment_create'),
]
