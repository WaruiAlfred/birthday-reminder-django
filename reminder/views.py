from .models import Birthdays
from .serializers import BirthdaySerializer, BirthdayDataSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class BirthdaysView(viewsets.ModelViewSet):
    queryset = Birthdays.objects.all()
    serializer_class = BirthdaySerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BirthdaysDataView(viewsets.ModelViewSet):
    queryset = Birthdays.objects.all()
    serializer_class = BirthdayDataSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
