# Generated by Django 4.2.6 on 2023-10-14 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_profile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default=1, max_length=150, verbose_name='العنوان بالتفصيل'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='number_phone',
            field=models.CharField(default=1, max_length=150, verbose_name=' رقم الهاتف'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='specialist',
            field=models.CharField(default=1, max_length=50, verbose_name='التخصص'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='subtitle',
            field=models.CharField(default=1, max_length=150, verbose_name='نبذة عنك'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='waiting_time',
            field=models.IntegerField(blank=True, default=1, verbose_name='مدة الانتظار'),
        ),
        migrations.AddField(
            model_name='profile',
            name='working_hours',
            field=models.IntegerField(blank=True, default=1, verbose_name='عدد ساعات العمل'),
        ),
    ]