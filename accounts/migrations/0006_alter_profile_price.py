# Generated by Django 4.2.6 on 2023-10-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='price',
            field=models.IntegerField(blank=True, default=1, verbose_name='سعر الكشف '),
        ),
    ]
