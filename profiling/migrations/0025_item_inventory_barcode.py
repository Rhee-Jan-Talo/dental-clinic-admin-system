# Generated by Django 3.2.7 on 2021-10-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0024_remove_item_inventory_barcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_inventory',
            name='barcode',
            field=models.CharField(default='00000000', max_length=100),
        ),
    ]