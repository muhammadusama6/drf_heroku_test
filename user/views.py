from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     return Response({'message': 'User created successfully'},
    #                     status=status.HTTP_201_CREATED)

    def create(self, request, *args, **kwargs):
        User.objects.create_user(username=request.POST['username'],
                                 password=request.POST['password'],
                                 email=request.POST['email'])
        return Response(data={'message': 'User created successfully'})

    def destroy(self, request, *args, **kwargs):
        username = kwargs.get('username')
        user = self.get_object()
        user.delete()
        return Response(data={'message': 'User deleted successfully'},
                        status=status.HTTP_204_NO_CONTENT)

    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return Response(data={'message': 'Login successful'},
                            status=status.HTTP_200_OK)
        else:
            return Response(data={'message': 'Invalid credentials'},
                            status=status.HTTP_401_UNAUTHORIZED)
