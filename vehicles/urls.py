from django.urls import path
from .views import VehiclesList,PurchaseVehicleView

urlpatterns = [
    path('vehicle-list', VehiclesList.as_view(), name='vehicle-list'),
    path('purchase', PurchaseVehicleView.as_view(), name='purchase'),
]