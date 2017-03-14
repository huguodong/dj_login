"""dj_User URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from demo import views as demo_views
from django.views import  static as static_file
from dj_User import  settings

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^staticfiles/(?P<path>.*)$',static_file.serve,{'document_root': settings.STATICFILES_DIRS, 'show_indexes': True}),
    url(r'^login/', demo_views.login, name='login'),
    url(r'^logout/', demo_views.logout, name='logout'),
    url(r'^register/', demo_views.register, name='register'),
    url(r'^index/', demo_views.index, name='register'),
]
