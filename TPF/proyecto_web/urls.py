from django.urls import path
from proyecto_web import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('registro', views.registro, name='registro'),
    path('contacto', views.contacto, name='contacto')
]
