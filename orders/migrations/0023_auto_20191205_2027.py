# Generated by Django 2.2.4 on 2019-12-05 20:27

from django.db import migrations, models
import orders.models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_auto_20191205_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='url',
            field=models.CharField(default=orders.models.image, max_length=1000),
        ),
    ]
