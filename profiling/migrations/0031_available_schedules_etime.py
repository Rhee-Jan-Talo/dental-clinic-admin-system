# Generated by Django 3.2.7 on 2021-11-23 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0030_remove_prescription_management_presc_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='available_schedules',
            name='etime',
            field=models.TimeField(null=True),
        ),
    ]