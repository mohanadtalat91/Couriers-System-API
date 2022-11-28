# Generated by Django 4.1.3 on 2022-11-27 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0017_waybill_shipment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='waybill',
            name='destination_mobile',
        ),
        migrations.AddField(
            model_name='waybill',
            name='receiver_mobile',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='waybill',
            name='receiver_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]