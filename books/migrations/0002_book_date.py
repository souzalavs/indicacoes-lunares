# Generated by Django 4.1.7 on 2023-03-25 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
