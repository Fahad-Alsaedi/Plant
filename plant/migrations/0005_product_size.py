# Generated by Django 3.1.6 on 2021-02-23 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0004_remove_orderdetail_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='add', max_length=100),
            preserve_default=False,
        ),
    ]
