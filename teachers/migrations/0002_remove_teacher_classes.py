# Generated by Django 4.1.5 on 2023-01-14 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("teachers", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="teacher",
            name="classes",
        ),
    ]