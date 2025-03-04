# Generated by Django 4.2.4 on 2023-08-14 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_alter_user_managers_remove_user_groups_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('description', models.TextField(blank=True, null=True)),
                ('completion', models.BooleanField(default=False)),
                ('due_date', models.DateTimeField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'ordering': ['completion'],
            },
        ),
    ]
