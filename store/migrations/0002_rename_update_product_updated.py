# Generated by Django 5.0 on 2023-12-09 06:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="update",
            new_name="updated",
        ),
    ]
