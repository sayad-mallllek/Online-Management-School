# Generated by Django 4.1.5 on 2023-01-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_rename_parent_guardian"),
    ]

    operations = [
        migrations.AlterField(
            model_name="guardian",
            name="email",
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
