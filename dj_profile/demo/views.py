# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from  demo.models import Account
from django.contrib.auth.hashers import make_password, check_password
import json
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
import re


# Create your views here.
# 主页
@login_required
def index(request):
    user = request.user
    return render(request, 'index.html', locals())


# 注销
@login_required()
def logout(request):
    auth.logout(request)  # 注销
    return render(request, 'logout.html')


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username'].encode('utf8')
        password = request.POST['password'].encode('utf8')
        if username != None and password != None:
            user = auth.authenticate(username=username, password=password)  # 调用登录方法
            if user is not None and user.is_active:
                # if user.is_staff == 1:
                auth.login(request, user)  # 登录
                state = 1  # 登陆成功
                # else:
                #     state = 3  # 没有权限
            else:
                state = 2  # 登陆失败
        else:
            state = 0  # 非法输入
    return HttpResponse(json.dumps({"state": state}))


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username'].encode('utf8')
        password = request.POST['password'].encode('utf8')
        email = request.POST['email']
        # str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        # match = re.match(str, email)
        # if len(username) < 4 and len(username) > 16 and len(password) < 6 and match is None:  # 判断合法输入
        #     state = 0;
        #     return HttpResponse(json.dumps({"state": state}))
        if username != None and password != None and email != None:
            isReg = User.objects.filter(username=username).count()  # 检查重复
            if isReg == 0:
                # 注册
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                state = 1;  # 注册成功
                return HttpResponse(json.dumps({"state": state}))
            else:
                state = 2;  # 用户已存在
                return HttpResponse(json.dumps({"state": state}))
        return render(request, 'login.html')


@login_required()
@permission_required('demo.view_car',raise_exception=True)
def car(request):
    return render(request, 'car.html')
