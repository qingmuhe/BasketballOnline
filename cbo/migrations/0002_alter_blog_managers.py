# Generated by Django 4.2.7 on 2023-12-07 10:08

import cbo.models
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("cbo", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="blog",
            managers=[
                ("objects", cbo.models.UserManager()),
            ],
        ),
    ]
