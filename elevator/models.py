from django.db import models

# Create your models here.
class Elevator(models.Model):
    num_floors = models.IntegerField()
    current_floor = models.IntegerField(default=1)
    direction = models.CharField(max_length=10, default="STOPPED")
    destinations = models.ManyToManyField("Floor", blank=True)
    door_open = models.BooleanField(default=False)
    is_running = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    is_operational = models.BooleanField(default=True)

    def __str__(self):
        return f"Elevator {self.id}"

class Floor(models.Model):
    floor_number = models.IntegerField()

    def __str__(self):
        return f"Floor {self.floor_number}"
