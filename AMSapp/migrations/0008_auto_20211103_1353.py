# Generated by Django 3.2.9 on 2021-11-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMSapp', '0007_auto_20211103_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timings',
            name='id',
        ),
        migrations.AddField(
            model_name='timings',
            name='timeId',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
