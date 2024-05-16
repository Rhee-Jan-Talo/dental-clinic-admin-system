# Generated by Django 3.2.7 on 2021-09-28 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0019_teeths_teeth_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='teeths',
            name='L1PM_left',
            field=models.CharField(default='Lower 1st Premolar(Right)', max_length=200),
        ),
        migrations.AddField(
            model_name='teeths',
            name='L1PM_right',
            field=models.CharField(default='Lower 1st Premolar(Left)', max_length=200),
        ),
        migrations.AddField(
            model_name='teeths',
            name='L2PM_left',
            field=models.CharField(default='Lower 2nd Premolar(Right)', max_length=200),
        ),
        migrations.AddField(
            model_name='teeths',
            name='L2PM_right',
            field=models.CharField(default='Lower 2nd Premolar(Left)', max_length=200),
        ),
        migrations.AddField(
            model_name='teeths',
            name='LTM_left',
            field=models.CharField(default='Lower Third Molar(Right)', max_length=200),
        ),
        migrations.AddField(
            model_name='teeths',
            name='LTM_right',
            field=models.CharField(default='Lower Third Molar(Left)', max_length=200),
        ),
        migrations.AddField(
            model_name='teeths',
            name='U1PM_left',
            field=models.CharField(default='Upper 1st Premolar(Left)', max_length=200),
        ),
        migrations.AddField(
            model_name='teeths',
            name='U1PM_right',
            field=models.CharField(default='Upper 1st Premolar(Right)', max_length=200),
        ),
        migrations.AddField(
            model_name='teeths',
            name='U2PM_left',
            field=models.CharField(default='Upper 2nd Premolar(Left)', max_length=200),
        ),
        migrations.AddField(
            model_name='teeths',
            name='U2PM_right',
            field=models.CharField(default='Upper 2nd Premolar(Right)', max_length=200),
        ),
        migrations.AddField(
            model_name='teeths',
            name='UTM_left',
            field=models.CharField(default='Upper Third Molar(Left)', max_length=200),
        ),
        migrations.AddField(
            model_name='teeths',
            name='UTM_right',
            field=models.CharField(default='Upper Third Molar(Right)', max_length=200),
        ),
    ]
