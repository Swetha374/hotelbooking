# Generated by Django 4.0.6 on 2022-11-13 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='hotel_name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
