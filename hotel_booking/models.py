from django.db import models
from django.contrib.auth.models import User  


class Hotel_Model(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    total_rooms = models.IntegerField()  
    available_rooms = models.IntegerField()  
    photos = models.ImageField(upload_to='hotel/images')
    rating = models.FloatField() 

    def __str__(self):
        return self.name


class Room_Model(models.Model):
    hotel = models.ForeignKey(Hotel_Model, on_delete=models.CASCADE) 
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photos = models.ImageField(upload_to='room/images')
    is_available = models.BooleanField(default=True)  
    def __str__(self):
        return f'Room {self.room_number} at {self.hotel.name}'


class Booking_Model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room_Model, on_delete=models.CASCADE)  
    check_in = models.DateField()
    check_out = models.DateField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)  

    def __str__(self):
        return f'Booking by {self.user.username} for {self.room.hotel.name} - Room {self.room.room_number}'


class Review_Model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    hotel = models.ForeignKey(Hotel_Model, on_delete=models.CASCADE)
    ratings = models.IntegerField()  
    comment = models.TextField()

    def __str__(self):
        return f'Review by {self.user.username} for {self.hotel.name}'
