# Generated by Django 4.2.7 on 2023-11-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_coupe_sedan'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
