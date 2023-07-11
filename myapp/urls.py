from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    # path('',views.index,name='home'),
    # path('submit',views.details,name='submitrecord'),
    # path('list',views.list,name='listeddata'),
    # path('login',views.loginpage,name='loginpage'),
    # path('register',views.registerpage,name='registerpage'),
    # path('logout',views.logoutview,name='logoutuser'),


    path('',views.index,name='home'),
    path('login',views.loginpage,name='loginpage'),
    path('register',views.registerpage,name='registerpage'),
    path('submit',views.details,name='submitrecord'),
    path('list',views.list,name='listeddata'),
    path('ypost',views.userposts,name='userpost'),
    path('logout',views.logoutview,name='logoutuser'),
    path('delete/<str:id>',views.remove,name='deleteuserpost'),
]
