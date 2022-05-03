from django.db import models
from django.contrib.auth.models import User


class Birthdays(models.Model):
    user = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)
    friends_name = models.CharField(max_length=100)
    year_of_birth = models.IntegerField(default=2000)
    month_of_birth = models.IntegerField(default=11)
    day_of_birth = models.IntegerField(default=12)
    DisplayFields = [
        "id",
        "user",
        "friends_name",
        "year_of_birth",
        "month_of_birth",
        "day_of_birth",
    ]

    def __str__(self):
        return self.friends_name
