# Generated by Django 4.2.6 on 2023-10-21 19:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0017_remove_profile_is_doctor_profile_patient'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile_Patient',
            new_name='ProfilePatient',
        ),
        migrations.AlterModelOptions(
            name='profilepatient',
            options={'verbose_name': 'الملف الشخصي', 'verbose_name_plural': ' المرضى  '},
        ),
        migrations.AddField(
            model_name='profile',
            name='is_doctor',
            field=models.BooleanField(auto_created=True, default=1),
            preserve_default=False,
        ),
    ]
