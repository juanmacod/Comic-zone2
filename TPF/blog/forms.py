from django.forms import ModelForm
from .models import Post, Comentario

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen', 'categorias']

class Comentario_Form(ModelForm):
    class Meta:
        model = Comentario
        fields = ('contenido',) 
        