# Generated by Django 3.1.7 on 2021-05-06 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Asha', '0014_familymembers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Gender', models.CharField(max_length=5)),
                ('DOB', models.DateField()),
                ('Auth_Id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Asha.basicdetails')),
            ],
        ),
    ]
