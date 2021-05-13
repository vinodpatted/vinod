"""carservice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from car import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.carview),
    path('list',views.carlist.as_view(), name='list'),
    re_path('^(?P<pk>\d+)/$',views.cardetail.as_view()),
    re_path('create',views.carcreate.as_view()),
    re_path('update/(?P<pk>\d+)/$',views.carupdate.as_view()),
    re_path('delete/(?P<pk>\d+)/$',views.cardelete.as_view()),
    re_path('/pdf',views.GeneratePdf.as_view(), name='pdf')
]
