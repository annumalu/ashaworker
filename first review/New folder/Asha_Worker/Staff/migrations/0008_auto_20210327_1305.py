# Generated by Django 3.0.8 on 2021-03-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0007_asha_insurance'),
    ]

    operations = [
        migrations.AddField(
            model_name='asha_contact_user',
            name='Reply',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='asha_contact_user',
            name='Status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
