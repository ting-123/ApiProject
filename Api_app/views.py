from django.shortcuts import render
from Api_app.models import *
import time
from  django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import json

# Create your views here.
def v_help(request):
    return render(request,'help.html')

def sunshine(request):
    return render(request,'sunshine.html')

#进入登录页面的函数
def login(request,message=''): #message为空表示默认值，传值就用传的，不传就使用默认空。

    res = {}
    res["notice"] = list(DB_notice.objects.all().values('content'))[::-1][:2]
    res['message'] = message
    print(res)

    return render(request,'login.html',res)

#登录功能
def login_action(request):
    time.sleep(3)
    # 获取用户名密码
    username = request.POST.get('username',None)
    password = request.POST.get('password',None)
    print(username,password)
    # 去数据库进行比对是否正确
    user = auth.authenticate(username=username,password=password)
    if user is None:#用户名或密码错误
        return login(request,'用户名或密码错误')
    else:#登录成功，比对成功
        auth.login(request,user)
        request.session['user'] = username
        #跳转到首页
        return HttpResponseRedirect('/index/')

#注册功能
def register_action(request):
    time.sleep(3)
    # 获取用户输入的用户名和密码
    username = request.GET['username']
    password = request.GET['password']
    print(username,password)
    # 去数据库注册
    try:
        user = User.objects.create_user(username=username,password=password)
        user.save()
        #登录
        auth.login(request,user)
        request.session['user'] = username
        #跳转首页
        return HttpResponseRedirect('/index/')
    except:
        return login(request,'用户名已存在')
#退出功能
def logout(request):
    auth.logout(request)
    return  HttpResponseRedirect('/') #重定向到登录页面

#进入vue首页
@login_required()
def index(request):
    return render(request,'index.html')

#获取统计数据
def get_tj_datas(request):
    tj_datas = {}
    tj_datas['notices'] = list(DB_notice.objects.all().values('content'))[::-1]

    return HttpResponse(json.dumps(tj_datas),content_type='application/json')