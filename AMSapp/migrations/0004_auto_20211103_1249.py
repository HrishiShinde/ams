# Generated by Django 3.2.9 on 2021-11-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMSapp', '0003_timings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timings',
            name='userBrkIn',
            field=models.DateTimeField(default=0),
        ),
        migrations.AlterField(
            model_name='timings',
            name='userBrkOut',
            field=models.DateTimeField(default=0),
        ),
        migrations.AlterField(
            model_name='timings',
            name='userClkIn',
            field=models.DateTimeField(default=0),
        ),
        migrations.AlterField(
            model_name='timings',
            name='userClkOut',
            field=models.DateTimeField(default=0),
        ),
    ]
