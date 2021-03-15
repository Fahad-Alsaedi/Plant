# Generated by Django 3.1.7 on 2021-02-24 20:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('plant', '0010_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ara',
            field=models.CharField(default=datetime.datetime(2021, 2, 24, 20, 12, 40, 51645, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='place',
            field=models.CharField(default=datetime.datetime(2021, 2, 24, 20, 13, 1, 482991, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]