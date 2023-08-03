from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('crear_post', views.crear_post, name='crear_post'),
]
