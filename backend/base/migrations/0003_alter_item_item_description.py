# Generated by Django 5.1.1 on 2024-10-10 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
