# Generated by Django 3.1.7 on 2021-04-19 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Asha', '0011_auto_20210330_1022'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baby',
            name='Auth_Id',
        ),
        migrations.DeleteModel(
            name='User_Asha_Notifications',
        ),
        migrations.RemoveField(
            model_name='user_palliative',
            name='Auth_Id',
        ),
        migrations.RemoveField(
            model_name='user_pregnancy',
            name='Auth_Id',
        ),
        migrations.DeleteModel(
            name='Baby',
        ),
        migrations.DeleteModel(
            name='User_Palliative',
        ),
        migrations.DeleteModel(
            name='User_Pregnancy',
        ),
    ]
