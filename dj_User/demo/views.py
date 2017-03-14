# coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
from demo.models import *
from django.contrib.auth.hashers import make_password, check_password
from demo import PbMenthod as Pb
import json
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
# 主页
@login_required
def index(request):
    user = request.user
    return render(request, 'index.html', locals())


# 注销
def logout(request):
    auth.logout(request)#注销
    return render(request, 'logout.html', )


# 登录
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username'].encode('utf8')
        password = request.POST['password'].encode('utf8')
        if username != None and password != None:
            user = auth.authenticate(username=username, password=password)  # 调用登录方法
            if user is not None and user.UserState:
                auth.login(request, user)  # 登录
                state = 1  # 登陆成功
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
        email = request.POST['email'].encode('utf8')
        if len(username) < 4 and len(username) > 16 and len(password) < 6:#判断合法输入
            state = 0;
            return HttpResponse(json.dumps({"state": state}))
        if username != None and password != None and email != None:
            isReg = TB_User.objects.filter(UserName=username).count() #检查重复
            if isReg == 0:
                #注册
                user = TB_User()
                user.UID = Pb.CreateID()
                user.UserName = username
                user.UserPwd = user.hashed_password(password)
                user.UserEmail = email
                user.save()
                user = auth.authenticate(username=username, password=password)
                auth.login(request, user)
                state = 1;#注册成功
                return HttpResponse(json.dumps({"state": state}))
            else:
                state = 2;#用户已存在
                return HttpResponse(json.dumps({"state": state}))
        return render(request, 'login.html')
