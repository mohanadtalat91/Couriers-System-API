# Generated by Django 4.1.3 on 2022-11-27 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0002_courierman_rename_shipment_id_shipment_id_shipment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courierman',
            name='email',
        ),
        migrations.RemoveField(
            model_name='courierman',
            name='id_courier',
        ),
        migrations.RemoveField(
            model_name='courierman',
            name='mobile',
        ),
    ]
