# Generated by Django 2.0 on 2021-07-17 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0070_auto_20210718_0023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmodel',
            name='Admin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='chats.Profile'),
        ),
    ]