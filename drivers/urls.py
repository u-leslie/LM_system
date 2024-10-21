from django.urls import path
from . import views

urlpatterns = [
    path('', views.driver_list, name='drivers_list'),
    path('/drivers/create', views.driver_create, name='drivers_create'),
    path('edit/<int:pk>/', views.driver_edit, name='driver_edit'),  # Add this line
    path('delete/<int:pk>/', views.driver_delete, name='driver_delete'),  # Add this lin
    path('<int:pk>/', views.driver_detail, name='driver_detail'),
]
