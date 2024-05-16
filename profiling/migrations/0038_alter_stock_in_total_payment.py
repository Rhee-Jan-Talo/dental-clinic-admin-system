# Generated by Django 3.2.7 on 2021-11-26 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0037_item_inventory_tot_spent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_in',
            name='total_payment',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]