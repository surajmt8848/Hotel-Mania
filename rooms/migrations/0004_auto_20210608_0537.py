# Generated by Django 3.2.3 on 2021-06-08 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_auto_20210516_0546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='room',
            name='lng',
        ),
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='RS per night', max_digits=10),
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
