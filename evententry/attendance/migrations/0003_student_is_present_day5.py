# Generated by Django 4.2.11 on 2024-04-22 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_activeday'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_present_day5',
            field=models.BooleanField(default=False),
        ),
    ]
