# Generated by Django 5.0.6 on 2024-06-22 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_deliveryaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliveryaddress',
            name='pincode',
            field=models.CharField(max_length=6),
        ),
    ]
