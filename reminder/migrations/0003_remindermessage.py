# Generated by Django 4.0.4 on 2022-05-03 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reminder", "0002_alter_birthdays_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReminderMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message", models.CharField(max_length=100)),
            ],
        ),
    ]