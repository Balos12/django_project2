# Generated by Django 4.0.4 on 2023-04-23 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0003_women_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='women',
            name='user',
        ),
    ]
