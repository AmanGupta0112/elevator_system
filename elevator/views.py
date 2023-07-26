from rest_framework import viewsets
from .models import Elevator, Floor
from .serializers import ElevatorSerializer, FloorSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    @action(detail=True, methods=['post'])
    def move_up(self, request, pk=None):
        elevator = self.get_object()
        elevator.move_up()
        return Response("Elevator is moving up.")

    @action(detail=True, methods=['post'])
    def move_down(self, request, pk=None):
        elevator = self.get_object()
        elevator.move_down()
        return Response("Elevator is moving down.")

    @action(detail=True, methods=['post'])
    def open_door(self, request, pk=None):
        elevator = self.get_object()
        elevator.open_door()
        return Response("Elevator door is opened.")

    @action(detail=True, methods=['post'])
    def close_door(self, request, pk=None):
        elevator = self.get_object()
        elevator.close_door()
        return Response("Elevator door is closed.")

    @action(detail=True, methods=['post'])
    def start_running(self, request, pk=None):
        elevator = self.get_object()
        elevator.start_running()
        return Response("Elevator is running.")

    @action(detail=True, methods=['post'])
    def stop_running(self, request, pk=None):
        elevator = self.get_object()
        elevator.stop_running()
        return Response("Elevator has stopped running.")

    @action(detail=True, methods=['get'])
    def display_status(self, request, pk=None):
        elevator = self.get_object()
        status = {
            "elevator_id": elevator.id,
            "current_floor": elevator.current_floor,
            "direction": elevator.direction,
            "door_open": elevator.door_open,
            "is_running": elevator.is_running,
            "is_available": elevator.is_available,
            "is_operational": elevator.is_operational,
        }
        return Response(status)

    @action(detail=True, methods=['post'])
    def associate_floor(self, request, pk=None):
        elevator = self.get_object()
        floor_number = request.query_params.get('floor_number')
        if floor_number is not None:
            elevator.associate_floor(int(floor_number))  # Convert 'floor_number' to an integer
            return Response(f"Elevator {elevator.id} associated with Floor {floor_number}.")
        else:
            return Response("Please provide a valid 'floor_number' as a query parameter.", status=400)

    @action(detail=True, methods=['post'])
    def mark_available(self, request, pk=None):
        elevator = self.get_object()
        elevator.mark_available()
        return Response(f"Elevator {elevator.id} is marked available.")

    @action(detail=True, methods=['post'])
    def mark_operational(self, request, pk=None):
        elevator = self.get_object()
        elevator.mark_operational()
        return Response(f"Elevator {elevator.id} is marked operational.")

    @action(detail=True, methods=['post'])
    def mark_not_operational(self, request, pk=None):
        elevator = self.get_object()
        elevator.mark_not_operational()
        return Response(f"Elevator {elevator.id} is marked not operational.")
    
    @action(detail=True, methods=['post'])
    def create_user_request(self, request, pk=None):
        floor_number = request.query_params.get('floor_number')
        if floor_number is not None:
            try:
                floor_number = int(floor_number)
            except ValueError:
                return Response("Invalid floor_number. Please provide an integer.", status=400)
            
            elevator = self.get_object()
            elevator.save_user_request(floor_number)
            return Response(f"User request to Floor {floor_number} added to Elevator {elevator.id}.")
        else:
            return Response("Please provide 'floor_number' in the request data.", status=400)
        
    
    @action(detail=True, methods=['get'])
    def get_next_destination(self, request, pk=None):
        elevator = self.get_object()
        next_destination = elevator.get_next_destination_floor()
        return Response({"elevator_id": elevator.id, "next_destination_floor": next_destination})
