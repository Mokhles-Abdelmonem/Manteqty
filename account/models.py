from django.db import models
from django.contrib.auth.models import AbstractUser

# user العادي
class User(AbstractUser):
    # ودا معانه أنا مش عاوز username نهائي"
    username = None

    # كل مستخدم لازم يكون عنده email مختلف
    email = models.EmailField(unique=True)

    # إيه الحقل الأساسي اللي المستخدم هيسجل بيه الدخول؟
    USERNAME_FIELD = 'email'
    # يعني مفيش حقول إضافية إجبارية وقت إنشاء user
    # "إيه الحقول الإضافية المطلوبة وقت إنشاء superuser
    REQUIRED_FIELDS =['phone_number']

    # دي بتحدد أنواع المستخدمين
    Role_CHOICES = (
        ("user", "User"),
        ("service_provider", "Service_provider"),
    )


    phone_number = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    role = models.CharField(
        max_length = 100,
        choices = Role_CHOICES,
        default = "user",
    #     ودا كل user لازم يكون نوع معين من اللي انا عاملهم
    )


# userالمستخدم صاحب الخدمة
class Serviceprofile(models.Model):
    # اولا الرابط بي user
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    location = models.CharField(max_length = 100)
    working_hours = models.IntegerField()
    description = models.TextField()


class location(models.Model):
    pass


# Create your models here.






# **============================**
# **================================**
#الاول: الحسابات (Accounts)
# كمستخدم جديد
# أريد إنشاء حساب بسهولة باستخدام:
# رقم الهاتف
# أو
# البريد الإلكتروني
# حتى أتمكن من استخدام التطبيق.
#
# كصاحب خدمة
# أريد إنشاء صفحة خاصة بخدمتي تحتوي على:
# اسم النشاط
# الصور
# الموقع
# أوقات العمل
# وصف الخدمة
# حتى يتمكن العملاء من الوصول إليّ.






