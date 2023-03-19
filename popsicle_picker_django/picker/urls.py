from django.urls import path
from . import views

urlpatterns = [
    path('', views.picker, name='home')
]