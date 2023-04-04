from rest_framework import viewsets
from rest_framework.response import Response

from .models import TestApi
from .serializers import TestApiSerializer


class TestApiViewSet(viewsets.ModelViewSet):
    model = TestApi
    queryset = model.objects.all()
    serializer_class = TestApiSerializer

    def create(self, request, *args, **kwargs):
        roll = TestApi.objects.create(
            rollNum=request.data['rollNum'],
        )
        return Response(data={ 'task added'})
