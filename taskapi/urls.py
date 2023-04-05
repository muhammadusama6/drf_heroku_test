from django.urls import path, include
from rest_framework import routers
from .views import TasklistViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TasklistViewSet)

urlpatterns = [
    path('', include(router.urls))
]