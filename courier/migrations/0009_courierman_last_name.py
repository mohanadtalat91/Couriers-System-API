# Generated by Django 4.1.3 on 2022-11-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0008_remove_courierman_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='courierman',
            name='last_name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
