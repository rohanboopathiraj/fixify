# Generated by Django 3.2.25 on 2024-11-17 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_fixifyuser_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fixifyuser',
            name='username',
        ),
    ]