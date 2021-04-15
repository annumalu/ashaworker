# Generated by Django 3.1.7 on 2021-04-06 05:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('District_Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Org_Profile',
            fields=[
                ('Auth_Id', models.TextField(primary_key=True, serialize=False)),
                ('DOB', models.DateField()),
                ('Gender', models.CharField(max_length=10)),
                ('State', models.CharField(max_length=50, null=True)),
                ('District', models.CharField(max_length=50, null=True)),
                ('Mobile', models.IntegerField()),
                ('image', models.ImageField(default='default.png', upload_to='Organizer/Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pan_Mun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Panchayath_Name', models.CharField(max_length=30)),
                ('District', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.district')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('State_Name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ward_Name', models.CharField(max_length=30)),
                ('Panchayath', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.pan_mun')),
            ],
        ),
        migrations.CreateModel(
            name='Org_Reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject', models.CharField(max_length=20)),
                ('Comment', models.TextField()),
                ('Report', models.FileField(upload_to='Organizer/Reports')),
                ('Date', models.DateField()),
                ('Auth_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.org_profile')),
            ],
        ),
        migrations.AddField(
            model_name='district',
            name='State',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.state'),
        ),
    ]
