from django.contrib import admin
from django.urls import path,include
from . import views
from AutoGarage import settings
from django.conf.urls.static import static
urlpatterns = [

    path('',views.index,name='index'),

]