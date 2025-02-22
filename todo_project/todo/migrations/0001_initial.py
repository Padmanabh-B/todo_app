# Generated by Django 5.1.6 on 2025-02-22 16:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
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
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True, null=True)),
                ("due_date", models.DateTimeField(default=django.utils.timezone.now)),
                ("completed", models.BooleanField(default=False)),
            ],
        ),
    ]
