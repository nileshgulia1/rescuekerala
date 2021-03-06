# Generated by Django 2.1 on 2018-08-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_auto_20180811_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('pro', 'In progess'), ('sup', 'Supplied')], default='new', max_length=10),
        ),
        migrations.AlterField(
            model_name='request',
            name='supply_details',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
