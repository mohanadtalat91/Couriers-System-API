# Generated by Django 4.1.3 on 2022-11-27 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0011_alter_courierman_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='courierman',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='courierman',
            name='last_name',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
