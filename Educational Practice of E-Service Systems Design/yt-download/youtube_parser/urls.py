from django.urls import path
from yt_parse import views

urlpatterns = [
    path('', views.index, name='index'),
]