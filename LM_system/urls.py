from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('shipments/', include('shipments.urls')),
    path('drivers/', include('drivers.urls')),
    path('deliveries/', include('deliveries.urls')),
]
