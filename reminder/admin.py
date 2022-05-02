from django.contrib import admin
from .models import Birthdays


class BirthdaysAdmin(admin.ModelAdmin):
    list_display = Birthdays.DisplayFields
    list_filter = (
        "user",
        "friends_name",
        "friends_birthdate",
    )


admin.site.register(Birthdays, BirthdaysAdmin)
