from rest_framework import serializers
from .models import Car,Bike,Truck,Customer,RentalRecord,Owner
from rest_framework import serializers

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class Carserializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
class Bikeserializer(serializers.ModelSerializer):
    class Meta:
        model= Bike
        fields='__all__'
class Truckserializer(serializers.ModelSerializer):
    class Meta:
        model=Truck
        fields='__all__'
class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'
class rentalRecordserializer(serializers.ModelSerializer):
    class Meta:
        model=RentalRecord
        fields='__all__'