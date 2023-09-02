"""ambroidery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include

from profile_ import views as viewspf
from about import views as viewsabout
from contact import views as viewscontact
from homepage import views as viewshm
from register import views as viewsrsg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login',viewsrsg.login,name='login'),
    path('',viewshm.homepage,name='homepage'),
    path('accounts/', include('allauth.urls')),
    path('profile/',viewsrsg.profile),
    path('about',viewsabout.about),
    path('contact',viewscontact.contact),
    path('signup',viewsrsg.register),
    path('challanin',viewsrsg.challanin),
    path('challanout',viewsrsg.challanout),
    path('party',viewsrsg.party),
    path('party/rm/<str:id>',viewsrsg.action),
    path('challanin/rm/<str:id>',viewsrsg.action2),
    path("genchallan",viewsrsg.genchallan)
    
    
]
