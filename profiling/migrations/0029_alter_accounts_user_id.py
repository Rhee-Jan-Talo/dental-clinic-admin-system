# Generated by Django 3.2.7 on 2021-10-11 03:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiling', '0028_alter_accounts_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='user_id',
            field=models.OneToOneField(db_constraint=False, default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
