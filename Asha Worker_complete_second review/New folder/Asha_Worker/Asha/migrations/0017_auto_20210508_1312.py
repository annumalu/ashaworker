# Generated by Django 3.1.7 on 2021-05-08 07:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Asha', '0016_user_asha_notifications_user_palliative_user_pregnancy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_Asha_Notifications',
        ),
        migrations.RemoveField(
            model_name='user_pregnancy',
            name='Auth_Id',
        ),
        migrations.DeleteModel(
            name='User_Palliative',
        ),
        migrations.DeleteModel(
            name='User_Pregnancy',
        ),
    ]
