# Generated by Django 5.0.2 on 2024-03-04 04:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('code', models.CharField(default='', max_length=150)),
                ('studio', models.CharField(default='', max_length=150)),
                ('deliveryDate', models.DateTimeField(default=datetime.datetime(2024, 3, 4, 4, 34, 41, 390187, tzinfo=datetime.timezone.utc))),
                ('thumbnail', models.CharField(default='', max_length=250)),
                ('img1', models.CharField(default='', max_length=250)),
                ('img2', models.CharField(default='', max_length=250)),
                ('img3', models.CharField(default='', max_length=250)),
                ('price', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]
