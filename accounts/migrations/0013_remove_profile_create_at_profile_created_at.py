# Generated by Django 4.2.6 on 2023-10-15 16:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_profile_create_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='create_at',
        ),
        migrations.AddField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='وقت الانضمام'),
            preserve_default=False,
        ),
    ]
