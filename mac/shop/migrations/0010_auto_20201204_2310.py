# Generated by Django 3.1.2 on 2020-12-04 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_orderupdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]