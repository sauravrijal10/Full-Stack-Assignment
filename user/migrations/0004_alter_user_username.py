# Generated by Django 4.2.4 on 2023-08-14 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=255),
        ),
    ]
