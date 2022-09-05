from django.urls import path,include
from . import views

urlpatterns = [

    path('regis',views.regis,name='regis'),
    path('login',views.login,name='login'),
    path('logout', views.logout, name='logout'),
    path('booking', views.booking, name='booking'),
    path('form', views.form, name='form'),
]