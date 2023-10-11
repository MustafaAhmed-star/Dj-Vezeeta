from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy  as _

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name =models.CharField(_('الاسم :'),max_length=40)
    who_iam = models.TextField(_("من انا :"),max_length=250)
    price = models.IntegerField(_("سعر الكشف : "))

    class Meta:
        # تحديد اسم الكلاس في admin panel 
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")
    def __str__(self):
        return self.name