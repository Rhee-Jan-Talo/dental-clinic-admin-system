# Generated by Django 3.2.7 on 2021-11-25 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0033_payment_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary_info',
            name='salary_type',
            field=models.CharField(default='Monthly Salary', max_length=100),
        ),
    ]