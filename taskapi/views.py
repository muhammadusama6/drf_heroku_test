from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Task
from .serializers import tasklistSerializer


class TasklistViewSet(viewsets.ModelViewSet):
    model = Task
    queryset = model.objects.all()
    serializer_class = tasklistSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Task created successfully'},
                        status=status.HTTP_201_CREATED)
