# Generated by Django 2.0 on 2021-07-05 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0052_auto_20210705_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forgotpwd',
            name='created_at',
            field=models.DateTimeField(default='2021-07-05 23:03:00.831350'),
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default='2021-07-05 23:03:00.831350'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_At',
            field=models.DateTimeField(default='2021-07-05 23:03:00.830353'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(default='2021-07-05 23:03:00.830353'),
        ),
    ]