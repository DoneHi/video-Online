from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import View
from django.db.models import Q
# from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import  sys
class IndexView(View):
    def get(self,request):
        cur_nav='index'
        return render(request, 'index.html')

class LoginView(View):
    def get(self,request):
        cur_nav='index'
        return render(request, 'login.html')

# class RegisterView(View):
#     def post(self,request):
#         UserItem=request.POST
#         username=UserItem.get('username')
#         password=UserItem.get('password')
#         age=UserItem.get('age')
#         phone=UserItem.get('phone')
#         print(request.POST.get('username'))
#         return render(request, 'index.html')