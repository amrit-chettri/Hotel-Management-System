from django.contrib import admin
from . models import Hotel_Model, Room_Model, Review_Model , Booking_Model 

# Register your models here.

admin.site.register(Hotel_Model)
admin.site.register(Room_Model)
admin.site.register(Booking_Model)
admin.site.register(Review_Model)

