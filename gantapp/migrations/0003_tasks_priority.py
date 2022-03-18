# Generated by Django 3.2.12 on 2022-02-23 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gantapp', '0002_auto_20220219_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='priority',
            field=models.CharField(choices=[(0, 'high'), (1, 'midle'), (2, 'low')], default='', max_length=50),
            preserve_default=False,
        ),
    ]
