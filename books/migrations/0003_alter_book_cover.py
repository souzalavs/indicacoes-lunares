# Generated by Django 4.1.7 on 2023-03-27 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='media/%Y/%m/%d/'),
        ),
    ]