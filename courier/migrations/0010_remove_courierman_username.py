# Generated by Django 4.1.3 on 2022-11-27 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0009_courierman_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courierman',
            name='username',
        ),
    ]