# Generated by Django 5.1.1 on 2024-10-06 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_description', models.TextField(blank=True)),
                ('item_price', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_sold', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('item_tags', models.ManyToManyField(related_name='items', to='base.itemtag')),
            ],
        ),
    ]
