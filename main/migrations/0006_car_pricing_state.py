# Generated by Django 4.2.7 on 2023-11-27 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_booking_booking_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='pricing_state',
            field=models.CharField(default='RegularPricingState', max_length=20),
        ),
    ]
