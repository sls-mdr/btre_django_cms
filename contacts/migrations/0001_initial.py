# Generated by Django 4.2.7 on 2023-11-16 10:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=255)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('contact_date', models.DateTimeField(default=datetime.datetime(2023, 11, 16, 10, 19, 17, 925816))),
                ('user_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
