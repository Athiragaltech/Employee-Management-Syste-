from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('',views.index),
    path('about',views.add),
    path('insert',views.insert),
    path('delete/<id>',views.delete),
    path('edit',views.edit),
    path('contact',views.edit1),
    path('edit/<id>',views.edit2),
    path('update/<id>',views.update)
    ]
