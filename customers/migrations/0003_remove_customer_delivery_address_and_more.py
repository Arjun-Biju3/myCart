# Generated by Django 5.0.6 on 2024-06-22 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_deliveryaddress_customer_delivery_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='delivery_address',
        ),
        migrations.DeleteModel(
            name='DeliveryAddress',
        ),
    ]
