# elevator/serializers.py

from rest_framework import serializers
from .models import Elevator, Floor

class FloorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Floor
        fields = "__all__"

class ElevatorSerializer(serializers.ModelSerializer):
    destinations = FloorSerializer(many=True, read_only=True)

    class Meta:
        model = Elevator
        fields = "__all__"
