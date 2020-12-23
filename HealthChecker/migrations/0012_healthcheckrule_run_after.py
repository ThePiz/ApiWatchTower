# Generated by Django 2.2.17 on 2020-12-22 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HealthChecker', '0011_healthcheckrecord_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcheckrule',
            name='run_after',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nexts', to='HealthChecker.HealthCheckRule'),
        ),
    ]
