# Generated by Django 4.1.5 on 2023-10-19 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_remove_book_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='', upload_to='book/images'),
        ),
    ]
