# Generated by Django 4.2.6 on 2023-10-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_options_alter_profile_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='static/defaults/profile.jpg', height_field=100, upload_to='profile', verbose_name='الصورة الشخصية', width_field=100),
        ),
    ]