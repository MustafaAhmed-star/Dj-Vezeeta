from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy  as _
from django.dispatch import receiver
from django.db.models.signals import post_save
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name =models.CharField(_('الاسم '),max_length=40)
    who_iam = models.TextField(_("من انا "),max_length=250)
    price = models.IntegerField(_("سعر الكشف "),blank = True,default=1)
    image = models.ImageField(_("الصورة الشخصية"), upload_to= "profile",blank=True,default='static/profile.jpg' )

    class Meta:
        # تحديد اسم الكلاس في admin panel 
        verbose_name = _("الملف الشخصي")
        verbose_name_plural = _("ملفات شخصية")
    def __str__(self):
        return self.name
    


 

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    print('instance',instance )
    if created:
        profile = Profile.objects.create(user=instance, name=instance.username)
         
