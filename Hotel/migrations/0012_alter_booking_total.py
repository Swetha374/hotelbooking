# Generated by Django 4.0.6 on 2022-11-29 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0011_remove_perdaybooking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
