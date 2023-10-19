from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy  as _
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify



GENDER= (
    ('male', 'ذكر'),
    ('female', 'انثى'),
)
specialist = (
    ('جلدية', 'جلدية'),
    ('اسنان', 'اسنان'),
    ('اطفال حديثي الولاد', 'اطفال حديثي الولاد'),
    ('مخ واعصاب', 'مخ واعصاب'),
    ('عظام', 'عظام'),
    ('نساء', 'نساء'),
    ('انف واذن وحنجرة', 'انف واذن وحنجرة'),
    ('قلب واوعية دموية', 'قلب واوعية دموية'),
    ('امراض دم', 'امراض دم'),
    ('جراحه', 'جراحه'),
    ('تجميل', 'تجميل'),
    
)
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("user"), on_delete=models.CASCADE)
    name =models.CharField(_('الاسم '),max_length=40)
    who_iam = models.TextField(_("من انا "),max_length=250)
    specialist = models.CharField(_("التخصص"),choices=specialist ,max_length=50,default='جلدية')
    subtitle = models.CharField(_("نبذة عنك"), max_length=150)
    number_phone = models.CharField(_(" رقم الهاتف"), max_length=150)
    address = models.CharField(_("العنوان بالتفصيل"), max_length=150)
    price = models.IntegerField(_("سعر الكشف "),blank = True,default=1)       
    working_hours = models.IntegerField(_("عدد ساعات العمل"),blank = True,default=1)
    facebook  = models.CharField(max_length = 150,blank = True)
    google  = models.CharField(max_length = 150,blank = True)
    twitter  = models.CharField(max_length = 150,blank = True)
    waiting_time = models.IntegerField(_("مدة الانتظار"),blank = True,default=1)
    image = models.ImageField(_("الصورة الشخصية"), upload_to= "profile",blank=True )
    gender = models.CharField(_("الجنس"), max_length=10,choices=GENDER,default='male')
    slug = models.SlugField(max_length=200 ,unique=True,blank=True,null=True)
    created_at = models.DateTimeField(_("وقت الانضمام"),auto_now_add=True)
    class Meta:
        # تحديد اسم الكلاس في admin panel 
        verbose_name = _("الملف الشخصي")
        verbose_name_plural = _("ملفات شخصية")
    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username,allow_unicode=True)
        super(Profile, self).save(*args, **kwargs)
 

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile.objects.create(user=instance, name=instance.username)
         
