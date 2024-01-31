from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import vehicles,Transaction
from .serializers import vehiclesSerializers, PurchaseFormSerializer
from rest_framework import generics


class VehiclesList(generics.ListAPIView):
    queryset = vehicles.objects.all()
    serializer_class = vehiclesSerializers

class PurchaseVehicleView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = PurchaseFormSerializer

