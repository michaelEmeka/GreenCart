# Generated by Django 5.1.1 on 2024-10-29 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenbin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bin',
            name='launch_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='bin',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]