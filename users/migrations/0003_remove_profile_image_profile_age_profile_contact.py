# Generated by Django 4.2.7 on 2023-11-11 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_profile_city"),
    ]

    operations = [
        migrations.RemoveField(model_name="profile", name="image",),
        migrations.AddField(
            model_name="profile",
            name="age",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="profile",
            name="contact",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
