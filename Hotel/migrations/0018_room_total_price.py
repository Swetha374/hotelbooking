# Generated by Django 4.0.6 on 2022-11-20 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0017_rename_price_room_price_of_adult_room_price_of_child_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='total_price',
            field=models.FloatField(default='0'),
            preserve_default=False,
        ),
    ]
