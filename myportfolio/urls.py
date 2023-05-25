from django.contrib import admin
from django.urls import path,include
from myportfolio import views

urlpatterns = [
    path('',views.index,name='home'),
    path('home',views.index,name='home'),
    path('about',views.about,name='about'),
    path('project',views.Project,name='project'),

]
