from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=50,verbose_name=u'昵称', default='')
    birthday = models.DateField(verbose_name='生日', default=datetime.now, null=True, blank=True)
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), max_length=6, default='female')
    password = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default='image/elliot.png', max_length=100)
    age=models.IntegerField(default=0)
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

class EmailVerifyRecord(models.Model):
    SEND_EMAIL_TYPE = (
            ('register', '注册'),
            ('forget', '找回密码'),
            ('update_email', '修改邮箱'),
        )

    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(choices=SEND_EMAIL_TYPE, max_length=30, verbose_name='验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '邮箱%s 验证码:%s' % (self.email, self.code)

    # def unread_nums(self):
    #     from operation.models import UserMessage
    #
    #     return UserMessage.objects.filter(user=self.id, has_read=False).count()