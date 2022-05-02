from django.db import models
from django.contrib.auth.models import User


class Birthdays(models.Model):
    user = models.ForeignKey(User, related_name="users", on_delete=models.CASCADE)
    friends_name = models.CharField(max_length=100)
    friends_birthdate = models.DateField()
    current_date = models.DateField(auto_now_add=True)
    DisplayFields = ["id", "user", "friends_name", "friends_birthdate", "current_date"]
    # year_of_birth = models.IntegerField(max_length=4)
    # month_of_birth = models.IntegerField(max_length=2)
    # day_of_birth = models.IntegerField(max_length=2)

    def __str__(self):
        return self.friends_name
