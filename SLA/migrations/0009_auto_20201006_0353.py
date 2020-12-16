# Generated by Django 3.0.10 on 2020-10-06 03:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
        ('SLA', '0008_impact_urgency'),
    ]

    operations = [
        migrations.AddField(
            model_name='impact',
            name='company_link',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='administrator.Company'),
        ),
        migrations.AddField(
            model_name='impact',
            name='impact_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='urgency',
            name='company_link',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='administrator.Company'),
        ),
        migrations.AddField(
            model_name='urgency',
            name='urgency_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]