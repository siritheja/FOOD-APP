# Generated by Django 3.1.5 on 2021-01-15 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='profile_picture.png', upload_to='profile_pictures'),
        ),
    ]
