"""
PythonLW URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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


from django.urls import path
from . import views

urlpatterns = [
    path('',            views.index,            name="social_home"),
    path('news/create', views.create_news,      name="social_create_news"),
    path('news',        views.news,             name="social_news"),
    path('log_in',      views.log_in,           name="social_log_in"),
    path('sign_up',     views.sign_up,          name="social_sign_up"),
    path('create_user', views.create_new_user,  name="social_create_user"),
    path('create_news', views.post_news,        name="social_post_news"),
]

