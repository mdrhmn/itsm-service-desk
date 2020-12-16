# Generated by Django 3.0.10 on 2020-10-06 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SLA', '0007_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urgency_val', models.IntegerField(default=-1)),
                ('priority_link', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='SLA.Priority')),
            ],
        ),
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('impact_val', models.IntegerField(default=-1)),
                ('priority_link', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='SLA.Priority')),
            ],
        ),
    ]