# Generated by Django 3.0.10 on 2020-10-06 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SLA', '0005_priority_priority_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Priority',
        ),
    ]