# Generated by Django 4.0.6 on 2022-11-09 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0005_rename_hotel_name_hotel_hotel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel',
            field=models.TextField(max_length=120, null=True),
        ),
    ]
