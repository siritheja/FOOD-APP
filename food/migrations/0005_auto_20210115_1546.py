# Generated by Django 3.1.5 on 2021-01-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_auto_20210115_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.flaticon.com/svg/static/icons/svg/1377/1377194.svg', max_length=500),
        ),
    ]
