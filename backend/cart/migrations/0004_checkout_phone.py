# Generated by Django 5.1.1 on 2024-10-10 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_checkout_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]