# Generated by Django 4.1.3 on 2022-11-27 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0016_courierman_id_courier_courierman_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='waybill',
            name='shipment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='courier.shipment'),
        ),
    ]