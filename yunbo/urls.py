"""yunbo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from haiwai import views as haiwai_views

admin.autodiscover()

urlpatterns = [
	url(r'^$',haiwai_views.my_view, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/',include(auth_urls, namespace='accounts')),
    url(r'^myview/$',haiwai_views.my_view, name ='myview'),
    url(r'^sign-up/$', haiwai_views.sign_up, name ='sign-up'),
    url(r'^login/$', haiwai_views.login_view, name ='login'),
    url(r'^logout/$', haiwai_views.logout_view, name ='logout'),
    url(r'^device-view/(.+)/$',haiwai_views.device_play_view, name ='device-view')
]
