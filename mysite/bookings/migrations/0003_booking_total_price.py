# Generated by Django 4.2.6 on 2023-11-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_booking_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
