# Generated by Django 4.0.5 on 2022-11-15 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_product_category'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='category',
            table='Categories',
        ),
    ]
