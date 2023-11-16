from django.db import models


class Policies(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()


class Room(models.Model):
    ROOM_TYPE_CHOICES = [
        ("1_bed", "1 Bed"),
        ("2_bed", "2 Bed"),
        ("master", "Master"),
        # Add other room types as needed
    ]
    policies = models.ForeignKey(
        Policies, on_delete=models.CASCADE, related_name="rooms"
    )

    price = models.FloatField()
    room_type = models.CharField(max_length=10, choices=ROOM_TYPE_CHOICES)
    is_booked = models.BooleanField(default=False)
    pass

    def __str__(self):
        booked_status = "Booked" if self.is_booked else "Available"
        return f"{dict(self.ROOM_TYPE_CHOICES)[self.room_type]} Room - {self.price} ({booked_status})"


class Reservation(models.Model):
    # room = models.ForeignKey(Room)
    # is_booked_by = models.ForeignKey(User)
    # can_cancel = models.BooleanField(default=False)
    pass
# - For hotel/Airbnb-like web app
# 	- Reservation
# 		- Shows the room
# 		- Number of Guest
# 		- Check in and check out
# 			- check in
# 			- check out
# 		- Policies
# 		- Facilities
# 		- Price
# 		- Benefits
# 	- Bookings
# 		- Current
# 			- can cancel
# 				- day before
# 			- room will be disabled from other customer
# 		- Completed
# 		- Cancelled
