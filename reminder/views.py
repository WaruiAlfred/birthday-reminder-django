from .models import Birthdays
from .serializers import BirthdaySerializer
from rest_framework import viewsets


class BirthdaysView(viewsets.ModelViewSet):
    queryset = Birthdays.objects.all()
    serializer_class = BirthdaySerializer
