from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Hotel_Model, Room_Model, Review_Model, Booking_Model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import BookingSerializer, HotelSerializer, ReviewSerializer, RoomSerializer

class HotelViewset(viewsets.ModelViewSet):
    queryset = Hotel_Model.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]


    @action(detail=True, methods=['get'])
    def reviews(self, request, pk=None):
        hotel = self.get_object()
        reviews = Review_Model.objects.filter(hotel=hotel)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room_Model.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication] 

    @action(detail=True, methods=['get'])
    def availability(self, request, pk=None):
        room = self.get_object()
        return Response({"is_available": room.is_available})


    def get_queryset(self):
        queryset = Room_Model.objects.all()
        hotel_id = self.request.query_params.get('hotel', None)
        if hotel_id:
            queryset = queryset.filter(hotel_id=hotel_id)
        return queryset


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking_Model.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication] 

    def create(self, request, *args, **kwargs):
        room_id = request.data.get('room')
        room = Room_Model.objects.get(id=room_id)

        if not room.is_available:
            return Response({"error": "Room is not available for booking"}, status=status.HTTP_400_BAD_REQUEST)

        response = super().create(request, *args, **kwargs)
        room.is_available = False
        room.save()
        return response

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        booking = self.get_object()
        room = booking.room
        room.is_available = True  
        room.save()
        booking.delete()
        return Response({"status": "Booking canceled, room is now available"}, status=status.HTTP_200_OK)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review_Model.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication] 