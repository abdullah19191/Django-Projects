# Generated by Django 4.2.4 on 2023-08-28 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vege", "0004_department_studentid_student"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="roll_number",
        ),
        migrations.AddField(
            model_name="student",
            name="address",
            field=models.TextField(default="Add Address Here", max_length=500),
        ),
    ]
