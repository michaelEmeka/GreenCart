# Generated by Django 5.1.1 on 2024-10-05 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_user_address_alter_onetimepassword_time_expired'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onetimepassword',
            name='time_expired',
        ),
    ]