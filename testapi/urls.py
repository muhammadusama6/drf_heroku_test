from django.urls import path, include
from rest_framework import routers
from .views import TestApiViewSet

router = routers.DefaultRouter()
router.register(r'roll', TestApiViewSet)

urlpatterns = [
    path('', include(router.urls))
]