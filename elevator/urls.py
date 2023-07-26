from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ElevatorViewSet, FloorViewSet
app_name = 'elevator'
router = DefaultRouter()
router.register(r'elevators', ElevatorViewSet)
router.register(r'floors', FloorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
