# Generated by Django 5.1.1 on 2024-09-27 15:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_onetimepassword_time_up_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetimepassword',
            name='time_expired',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 27, 15, 25, 4, 715061, tzinfo=datetime.timezone.utc)),
        ),
    ]
