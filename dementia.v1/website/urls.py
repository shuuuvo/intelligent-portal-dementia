"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from homepage import views
from django.contrib import admin
from django.urls import path, include

from django.views.static import serve
from django.urls import re_path as url
from django.conf import settings

urlpatterns = [
    
    path('', views.home, name="home"),
    path('dementia', views.dementia_view, name="dementia"),
    path('learning', views.learning_view, name="learning"),
    path('technologies', views.technologies_view, name="technologies"),
    path('news', views.research_view, name="news"),
    path('404', views.error404_view, name='error404'),

    path('forum/', include('forum.urls')),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('account/', include('account.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),

]
