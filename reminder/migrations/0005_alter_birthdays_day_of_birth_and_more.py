# Generated by Django 4.0.4 on 2022-05-03 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "reminder",
            "0004_delete_remindermessage_remove_birthdays_current_date_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="birthdays",
            name="day_of_birth",
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name="birthdays",
            name="month_of_birth",
            field=models.IntegerField(default=11),
        ),
        migrations.AlterField(
            model_name="birthdays",
            name="year_of_birth",
            field=models.IntegerField(default=2000),
        ),
    ]
