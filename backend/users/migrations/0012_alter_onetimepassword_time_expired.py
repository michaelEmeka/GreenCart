# Generated by Django 5.1.1 on 2024-09-27 15:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_onetimepassword_time_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetimepassword',
            name='time_expired',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 27, 15, 29, 46, 317143, tzinfo=datetime.timezone.utc)),
        ),
    ]
