from rest_framework import serializers
from .models import vehicles,Transaction

class vehiclesSerializers(serializers.ModelSerializer):
    class Meta:
        model = vehicles
        fields = ['id','brand','model','year','price','mileage','picture']


class PurchaseFormSerializer(serializers.ModelSerializer):
    class Meta:
       model = Transaction
       fields = ['buyer', 'seller', 'vehicle', 'quantity', 'price']        