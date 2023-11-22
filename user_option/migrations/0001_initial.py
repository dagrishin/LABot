# Generated by Django 3.0.5 on 2020-04-20 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeInterval",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "time_start",
                    models.CharField(
                        choices=[
                            ("0", "0:00"),
                            ("1", "1:00"),
                            ("2", "2:00"),
                            ("3", "3:00"),
                            ("4", "4:00"),
                            ("5", "5:00"),
                            ("6", "6:00"),
                            ("7", "7:00"),
                            ("8", "8:00"),
                            ("9", "9:00"),
                            ("10", "10:00"),
                            ("11", "11:00"),
                            ("12", "12:00"),
                            ("13", "13:00"),
                            ("14", "14:00"),
                            ("15", "15:00"),
                            ("16", "16:00"),
                            ("17", "17:00"),
                            ("18", "18:00"),
                            ("19", "19:00"),
                            ("20", "20:00"),
                            ("21", "21:00"),
                            ("22", "22:00"),
                            ("23", "23:00"),
                            ("24", "24:00"),
                        ],
                        default="12",
                        max_length=2,
                    ),
                ),
                (
                    "time_end",
                    models.CharField(
                        choices=[
                            ("0", "0:00"),
                            ("1", "1:00"),
                            ("2", "2:00"),
                            ("3", "3:00"),
                            ("4", "4:00"),
                            ("5", "5:00"),
                            ("6", "6:00"),
                            ("7", "7:00"),
                            ("8", "8:00"),
                            ("9", "9:00"),
                            ("10", "10:00"),
                            ("11", "11:00"),
                            ("12", "12:00"),
                            ("13", "13:00"),
                            ("14", "14:00"),
                            ("15", "15:00"),
                            ("16", "16:00"),
                            ("17", "17:00"),
                            ("18", "18:00"),
                            ("19", "19:00"),
                            ("20", "20:00"),
                            ("21", "21:00"),
                            ("22", "22:00"),
                            ("23", "23:00"),
                            ("24", "24:00"),
                        ],
                        default="18",
                        max_length=2,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_intervals",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Status",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("status1", models.IntegerField(default=300)),
                ("status2", models.IntegerField(default=900)),
                ("status3", models.IntegerField(default=2700)),
                ("status4", models.IntegerField(default=7200)),
                ("status5", models.IntegerField(default=18000)),
                ("status6", models.IntegerField(default=86400)),
                ("status7", models.IntegerField(default=259200)),
                ("status8", models.IntegerField(default=2592000)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_word_status",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RepeatAmount",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("words_per_day", models.IntegerField(default=10)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_repeats",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
