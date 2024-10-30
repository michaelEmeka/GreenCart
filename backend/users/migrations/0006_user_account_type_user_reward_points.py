# Generated by Django 5.1.1 on 2024-10-29 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_business_name_user_first_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='account_type',
            field=models.CharField(blank=True, default='business', max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='reward_points',
            field=models.IntegerField(default=0),
        ),
    ]
