from django.urls import path
from . import views

handler404 = 'SocialApp.views.error_404'

urlpatterns = [
    path('', views.index_view, name="social_home"),
    path('news/create', views.create_news_view, name="social_create_news"),
    path('news', views.news_view, name="social_news"),
    path('news/post/<int:id>', views.post_view, name="social_post"),
    path('login', views.login_view, name="social_login"),
    path('signup', views.signup_view, name="social_signup"),
    path('logout', views.logout_view, name="social_logout"),
    ]

