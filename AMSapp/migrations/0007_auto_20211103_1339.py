# Generated by Django 3.2.9 on 2021-11-03 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMSapp', '0006_auto_20211103_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timings',
            name='userBrkIn',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='timings',
            name='userBrkOut',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='timings',
            name='userClkIn',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='timings',
            name='userClkOut',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
