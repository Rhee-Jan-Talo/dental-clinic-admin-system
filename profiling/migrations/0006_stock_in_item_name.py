# Generated by Django 3.2.7 on 2021-09-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0005_remove_stock_in_date_added'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock_in',
            name='item_name',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
