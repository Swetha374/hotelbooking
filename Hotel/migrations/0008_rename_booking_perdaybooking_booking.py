# Generated by Django 4.0.6 on 2022-11-25 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0007_perdaybooking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perdaybooking',
            old_name='Booking',
            new_name='booking',
        ),
    ]
