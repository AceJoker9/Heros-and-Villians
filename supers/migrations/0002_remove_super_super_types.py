# Generated by Django 4.1.7 on 2023-03-29 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super',
            name='super_types',
        ),
    ]