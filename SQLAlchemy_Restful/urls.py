"""SQLAlchemy_Restful URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from app.apis.UsersAPI import *
from app.apis.HomeAPI import *
from django.contrib import admin
admin.autodiscover()


urlpatterns = [

    url(r'^admin/', admin.site.urls),

    #======== User Controller

    url(r'^$', UserModel_SelectAll, name='SelectAll'),
    url(r'^api/insert$', UserModel_Insert, name='Users_Insert'),
    url(r'^api/delete/(?P<pk>[0-9]+)$', UserModel_Delete, name='Users_Delete'),
    url(r'^api/update/(?P<pk>[0-9]+)$', UserMOdel_Update, name='Users_Delete'),
    url(r'^api/search/(?P<pk>[0-9]+)$', UserModel_Search, name='Users_Search'),
    url(r'^api/username/(?P<username>\w+)$', UserModel_SearchUsername , name='User_Username'),

    #======== Home Controller

    url(r'^api/login$', SignIn, name='Users_Signin'),

]
