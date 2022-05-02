from rest_framework import serializers
from .models import Birthdays


class BirthdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Birthdays
        fields = "__all__"
