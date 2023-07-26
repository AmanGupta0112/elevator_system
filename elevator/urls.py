from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElevatorViewSet, FloorViewSet
app_name = 'elevator'
router = DefaultRouter()
router.register(r'elevators', ElevatorViewSet)
router.register(r'floors', FloorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('elevators/<int:pk>/move_up/', ElevatorViewSet.as_view({'post': 'move_up'}), name='move_up'),
    path('elevators/<int:pk>/move_down/', ElevatorViewSet.as_view({'post': 'move_down'}), name='move_down'),
    path('elevators/<int:pk>/open_door/', ElevatorViewSet.as_view({'post': 'open_door'}), name='open_door'),
    path('elevators/<int:pk>/close_door/', ElevatorViewSet.as_view({'post': 'close_door'}), name='close_door'),
    path('elevators/<int:pk>/start_running/', ElevatorViewSet.as_view({'post': 'start_running'}), name='start_running'),
    path('elevators/<int:pk>/stop_running/', ElevatorViewSet.as_view({'post': 'stop_running'}), name='stop_running'),
    path('elevators/<int:pk>/display_status/', ElevatorViewSet.as_view({'get': 'display_status'}), name='display_status'),
    path('elevators/<int:pk>/associate_floor/', ElevatorViewSet.as_view({'post': 'associate_floor'}), name='associate_floor'),
    path('elevators/<int:pk>/mark_maintenance/', ElevatorViewSet.as_view({'post': 'mark_maintenance'}), name='mark_maintenance'),
    path('elevators/<int:pk>/mark_available/', ElevatorViewSet.as_view({'post': 'mark_available'}), name='mark_available'),
    path('elevators/<int:pk>/mark_operational/', ElevatorViewSet.as_view({'post': 'mark_operational'}), name='mark_operational'),
    path('elevators/<int:pk>/mark_not_operational/', ElevatorViewSet.as_view({'post': 'mark_not_operational'}), name='mark_not_operational'),
    path('elevators/<int:pk>/create_user_request/', ElevatorViewSet.as_view({'post': 'create_user_request'}), name='create_user_request'),
    path('elevators/<int:pk>/get_next_destination/', ElevatorViewSet.as_view({'get': 'get_next_destination'}), name='get_next_destination'),
]
