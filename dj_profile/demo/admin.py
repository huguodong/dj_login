from django.contrib import admin

# Register your models here.
# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from demo.models import *


class AccountInline(admin.StackedInline):
    model = Account
    verbose_name=u'个人信息'
    verbose_name_plural =u'个人信息'

    can_delete = False


class UserProfileAdmin(UserAdmin):
    inlines = [AccountInline, ]


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
