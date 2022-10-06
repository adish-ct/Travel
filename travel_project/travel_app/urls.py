
from django.urls import path
from . import views

urlpatterns = [

    path('', views.screen, name="screen"),

]
