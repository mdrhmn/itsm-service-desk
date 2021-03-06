# Generated by Django 3.0.10 on 2020-10-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SLA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriorityMatrix',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UrgencyName1', models.CharField(max_length=50)),
                ('UrgencyName2', models.CharField(max_length=50)),
                ('UrgencyName3', models.CharField(max_length=50)),
                ('ImpactName1', models.CharField(max_length=50)),
                ('ImpactName2', models.CharField(max_length=50)),
                ('ImpactName3', models.CharField(max_length=50)),
                ('UrgencyNumber1', models.IntegerField(blank=True, null=True)),
                ('UrgencyNumber2', models.IntegerField(blank=True, null=True)),
                ('UrgencyNumber3', models.IntegerField(blank=True, null=True)),
                ('ImpactNumber1', models.IntegerField(blank=True, null=True)),
                ('ImpactNumber2', models.IntegerField(blank=True, null=True)),
                ('ImpactNumber3', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='slatable',
            old_name='CompanyName',
            new_name='CompanyUserName',
        ),
        migrations.RemoveField(
            model_name='slatable',
            name='Day',
        ),
    ]
