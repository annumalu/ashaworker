# Generated by Django 3.0.8 on 2021-03-25 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_org_reports'),
    ]

    operations = [
        migrations.AddField(
            model_name='org_profile',
            name='District',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='org_profile',
            name='State',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
