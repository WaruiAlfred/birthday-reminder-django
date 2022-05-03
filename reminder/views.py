from .models import Birthdays
from .email import send_reminder_mail
from .serializers import BirthdaySerializer, BirthdayDataSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema

import datetime


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

@api_view(["GET"])
@schema(None)
def birthday_reminder(request):
    current_date = datetime.datetime.utcnow().strftime("%m-%d")
    message = "Today is not your friend(s) birthday."
    birthdays = Birthdays.objects.filter(user=request.user.id).all()

    if birthdays.exists():
        for birthday in birthdays:
            birthdate = datetime.datetime(
                birthday.year_of_birth, birthday.month_of_birth, birthday.day_of_birth
            ).strftime("%m-%d")
            if current_date == birthdate:
                send_reminder_mail(
                    request.user.username, birthday.friends_name, request.user.email
                )
                message = "Reminder sent"
            else:
                message = "Your friend(s) birthday is due."
    else:
        message = "You have no birthday entries.Enter some then try again"

    return Response({"message": message})
