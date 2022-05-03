from rest_framework import serializers
from .models import Birthdays


class BirthdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Birthdays
        fields = (
            "id",
            "friends_name",
            "year_of_birth",
            "month_of_birth",
            "day_of_birth",
        )


class BirthdayDataSerializer(serializers.ModelSerializer):
    # user = serializers.SlugRelatedField(read_only=True, slug_field="users")

    class Meta:
        model = Birthdays
        fields = "__all__"
