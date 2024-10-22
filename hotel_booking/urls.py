from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HotelViewset, RoomViewSet, BookingViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'hotels', HotelViewset)
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),  
]
