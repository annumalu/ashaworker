# Generated by Django 3.0.8 on 2021-03-26 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Staff', '0005_auto_20210325_1606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org_Asha_Forms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Owner', models.CharField(max_length=20)),
                ('Title', models.CharField(max_length=20)),
                ('Form', models.FileField(upload_to='Organizer/Documents/Forms')),
                ('Comments', models.TextField()),
                ('Date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Org_Asha_Notifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Owner', models.CharField(max_length=20)),
                ('Title', models.CharField(max_length=20)),
                ('Comments', models.TextField(null=True)),
                ('Description', models.TextField()),
                ('Date', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='asha_reports',
            name='Feedback',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='asha_reports',
            name='Status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
