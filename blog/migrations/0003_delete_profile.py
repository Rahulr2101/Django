# Generated by Django 3.2.16 on 2023-01-25 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_profile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
