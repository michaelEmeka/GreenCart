# Generated by Django 5.1.1 on 2024-09-24 03:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_onetimepassword_current_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetimepassword',
            name='time_up',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 24, 3, 32, 25, 187681, tzinfo=datetime.timezone.utc)),
        ),
    ]