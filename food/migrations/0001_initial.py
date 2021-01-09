# Generated by Django 3.1.5 on 2021-01-09 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_desc', models.CharField(max_length=200)),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]
