# Generated by Django 4.2.6 on 2023-10-21 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_alter_profile_specialist'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_doctor',
            field=models.BooleanField(default=False, verbose_name='هل انت دكتور'),
        ),
    ]
