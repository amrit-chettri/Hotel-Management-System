from . models import Hotel_Model, Room_Model, Review_Model , Booking_Model 
from rest_framework import serializers


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Hotel_Model
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Room_Model
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Review_Model
        fields = '__all__'                

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Booking_Model
        fields = '__all__'
