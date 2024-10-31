# Generated by Django 5.1.1 on 2024-10-29 23:24

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret', models.UUIDField(default=uuid.uuid4)),
                ('version', models.CharField(max_length=20)),
                ('architecture', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=70)),
                ('waste_count', models.IntegerField(default=0)),
            ],
        ),
    ]
