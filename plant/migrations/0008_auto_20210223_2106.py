# Generated by Django 3.1.6 on 2021-02-23 21:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0007_remove_orderdetail_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Native',
        ),
        migrations.RemoveField(
            model_name='product',
            name='soilType',
        ),
    ]
