from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('music/', views.music),
    path('chain/', views.chain),
    path('tupac/', views.tupac),
    path('joel/', views.joel),

]