# Generated by Django 3.2.3 on 2021-06-08 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20210608_0537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='address',
        ),
    ]
