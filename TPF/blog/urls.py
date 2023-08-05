from django.urls import path
from . import views


urlpatterns = [
    path('', views.blog, name='blog'),
    # path('crear_post', views.crear_post, name='crear_post'),
    path('<int:post_id>', views.post_detail, name='post_detail'),
        # crear noti vvvvvvvvvvvvvvvvv
    path('registrar_noticia/', views.CrearNoticia.as_view(), name='registrar_noticia'),
    #buscador
    path('buscar/', views.buscar_posts, name='buscar_inicio'),
    #comentario
    path('comentar/', views.comentar_post, name='comentar_post'),
    #borrar comentario
    path('borrar/<int:pk>', views.Borrar_comentario.as_view(), name='borrar_comentario'),
    #modificar
    path('modificar/<int:pk>',views.Modificar_comentario.as_view(), name='modificar_comentario')
]
