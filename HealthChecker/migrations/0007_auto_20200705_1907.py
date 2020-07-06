# Generated by Django 2.2.14 on 2020-07-05 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HealthChecker', '0006_auto_20200705_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthcheckrecord',
            name='error',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='healthcheckrecord',
            name='error_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='healthcheckrecord',
            name='success',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]
