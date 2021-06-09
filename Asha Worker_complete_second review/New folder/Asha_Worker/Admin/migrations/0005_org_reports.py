# Generated by Django 3.0.8 on 2021-03-24 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_pan_mun_ward'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org_Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=20)),
                ('Comment', models.TextField()),
                ('Report', models.FileField(upload_to='Organizer/Reports')),
                ('Date', models.DateField()),
                ('Auth_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.Org_Profile')),
            ],
        ),
    ]
