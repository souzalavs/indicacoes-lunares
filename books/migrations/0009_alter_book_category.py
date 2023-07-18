# Generated by Django 4.1.7 on 2023-06-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('CRIME', 'Crime'), ('CIÊNCIA', 'Ciência'), ('DRAMA', 'Drama'), ('FANTASIA', 'Fantasia'), ('FICÇÃO CIENTÍFICA', 'Ficção Científica'), ('MISTÉRIO', 'Mistério'), ('NACIONAIS', 'Nacionais'), ('ROMANCE', 'Romance'), ('ROMANCE DE ÉPOCA', 'Romance de Época'), ('SUSPENSE', 'Suspense'), ('TERROR', 'Terror')], default='', max_length=100),
        ),
    ]