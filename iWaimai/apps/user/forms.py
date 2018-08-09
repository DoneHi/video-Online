from django.shortcuts import render
from django import forms
from .models import UserProfile
from captcha.fields import CaptchaField
# Create your views here.

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    # captcha = CaptchaField(error_messages={'invalid': '验证码错误'})

class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid': '验证码错误'})


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


# url:user:user_info
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'age', 'gender', 'birthday', 'mobile']