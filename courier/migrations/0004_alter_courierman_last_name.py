# Generated by Django 4.1.3 on 2022-11-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0003_remove_courierman_email_remove_courierman_id_courier_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courierman',
            name='last_name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
