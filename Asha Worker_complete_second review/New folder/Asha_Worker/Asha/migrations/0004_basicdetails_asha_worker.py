# Generated by Django 3.0.8 on 2021-03-24 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Asha', '0003_basicdetails_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicdetails',
            name='Asha_Worker',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
