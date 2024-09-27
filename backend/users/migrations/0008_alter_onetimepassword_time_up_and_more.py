# Generated by Django 5.1.1 on 2024-09-25 00:31

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_onetimepassword_current_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onetimepassword',
            name='time_up',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 25, 0, 32, 9, 213772, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='onetimepassword',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
