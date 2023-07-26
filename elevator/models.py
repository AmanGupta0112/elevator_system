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
    
    def stop_running(self):
        self.direction = "STOPPED"
        self.is_running = False
        self.save()

    def start_running(self):
        self.direction = "START"
        self.is_running = True
        self.save()

    def open_door(self):
        self.door_open = True
        self.save()

    def close_door(self):
        self.door_open = False
        self.save()

    def fetch_requests(self):
        return self.destinations.all()

    def fetch_next_destination(self):
        self.close_door()
        if self.destinations.exists():
            return min(self.destinations.all()) if self.direction == "UP" else max(self.destinations.all())
        return None

    def is_moving_up(self):
        self.close_door()
        return self.direction == "UP"

    def save_user_request(self, floor_number):
        self.destinations.add(floor_number)
        self.is_available = False
        self.save()

    def mark_maintenance(self):
        self.is_operational = False
        self.is_available = False
        self.stop_running()
        self.save()
    
    def associate_floor(self, floor_number):
        # Mark the elevator as unavailable when associated with a floor
        self.is_available = False
        self.save()

        # Add the floor to the destinations of the elevator
        floor, created = Floor.objects.get_or_create(floor_number=floor_number)
        self.destinations.add(floor)
        self.save()

    def mark_available(self):
        # Mark the elevator as available and clear destinations when idle
        self.is_available = True
        self.is_operational = True
        self.start_running()
        self.destinations.clear()
        self.save()

    def mark_operational(self):
        # Mark the elevator as operational
        self.is_operational = True
        self.save()

    def mark_not_operational(self):
        # Mark the elevator as not operational
        self.is_operational = False
        self.save()
    
    def save_user_request(self, floor_number):
        self.destinations.add(floor_number)
        self.is_available = False
        self.save()
    
    def get_next_destination_floor(self):
        if self.destinations.exists():
            floor_numbers = [floor.floor_number for floor in self.destinations.all()]
            if self.direction == "UP":
                next_floor = min(floor_numbers, default=None)
                if next_floor is not None and next_floor > self.current_floor:
                    return next_floor
            else:
                next_floor = max(floor_numbers, default=None)
                if next_floor is not None and next_floor < self.current_floor:
                    return next_floor

        return self.current_floor

    def move_up(self):
        if self.destinations.exists():
            self.direction = "UP"

            next_destination = self.get_next_destination_floor()
            if next_destination > self.current_floor:
                self.current_floor = next_destination
                self.destinations.remove(next_destination)  # Remove reached floor from destinations
                self.open_door()
            else:
                self.direction = "STOPPED"
        else:
            self.direction = "STOPPED"
        self.is_running = False
        self.save()

    def move_down(self):
        if self.destinations.exists():
            self.direction = "DOWN"
            next_destination = self.get_next_destination_floor()
            if next_destination < self.current_floor:
                self.current_floor = next_destination
                self.destinations.remove(next_destination)  # Remove reached floor from destinations
                self.open_door()
            else:
                self.direction = "STOPPED"
        else:
            self.direction = "STOPPED"
        self.is_running = False
        self.save()

class Floor(models.Model):
    floor_number = models.IntegerField()

    def __str__(self):
        return f"Floor {self.floor_number}"
