# Generated by Django 3.2.7 on 2021-11-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMSapp', '0009_auto_20211105_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='timings',
            name='hasHalfDayAppointed',
            field=models.BooleanField(default=False),
        ),
    ]
