# Generated by Django 3.0.10 on 2020-10-05 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SLA', '0004_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='priority',
            name='priority_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
