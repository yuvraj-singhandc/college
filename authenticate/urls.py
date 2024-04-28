from django.urls import path
from authenticate import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('login', views.loginuser, name = 'loginuser'),
    path('logout', views.logoutuser, name = 'logoutuser'),
    path('signup', views.signup, name = 'signup'),
    path('sign-in', views.signin, name = 'signin')
]
