from rest_framework import serializers
from .models import Birthdays


class BirthdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Birthdays
        fields = ("id", "friends_name", "friends_birthdate", "current_date")


class BirthdayDataSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, slug_field="users")

    class Meta:
        model = Birthdays
        fields = ("id", "user", "friends_name", "friends_birthdate", "current_date")
