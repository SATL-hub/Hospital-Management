# Generated by Django 5.1.2 on 2024-11-05 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0025_remove_profile_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='country',
        ),
    ]
