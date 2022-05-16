from .serializers import MyTokenObtainPairSerializer, RegisterSerializer,UsersDataSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics,viewsets
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    
class UsersDataView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersDataSerializer
    filterset_fields = ['username']
