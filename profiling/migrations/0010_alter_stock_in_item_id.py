# Generated by Django 3.2.7 on 2021-09-25 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0009_alter_stock_in_item_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock_in',
            name='item_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiling.item_inventory'),
        ),
    ]