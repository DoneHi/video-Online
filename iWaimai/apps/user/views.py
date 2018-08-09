from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.views import View

from .forms import RegisterForm
from .models import EmailVerifyRecord, UserProfile

from iWaimai.apps.utils import send_message
class ActiveUserView(View):
    # 页面get请求后直接查找激活码并激活对应账户
    def get(self, request, active_code):
        # 根据激活码查找对应的邮箱
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        # 如果查到激活码对应的邮箱
        if all_records:
            # 遍历所有符合条件的邮箱
            for record in all_records:
                record_email = record.email
                # 查找邮箱绑定的账户
                user = UserProfile.objects.get(email=record_email)
                # 激活账户
                user.is_active = True
                user.save()
        else:
            return render(request, '404.html')

        return render(request, 'login.html')


# 注册用户
class RegisterView(View):
    # get请求返回注册页面
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', locals())

    # post请求, 验证提交的表单
    def post(self, request):
        welcome_str_after_register = '欢迎注册'

        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            print('ss')
            user_name = request.POST.get('email', '')

            if UserProfile.objects.filter(username=user_name):
                msg = '用户名已存在'
                return render(request, 'index.html', locals())
            pass_word = request.POST.get('password', '')
            print(pass_word)
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.is_active = False
            # 使用django内置的哈希模块加密密码
            user_profile.password = make_password(pass_word)
            user_profile.save()

            send_message(
                user=user_profile,
                msg='欢迎您的注册!'
            )

            # 发送激活连接给邮箱
            # msg = send_register_email(user_name, 'register')
            return render(request, 'index.html', locals())

        else:
            return render(request, 'login.html', locals())