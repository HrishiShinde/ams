# Generated by Django 3.2.9 on 2021-11-08 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMSapp', '0015_alter_timings_numofhours'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='userClkIn',
            field=models.CharField(default='-', max_length=50),
        ),
    ]
