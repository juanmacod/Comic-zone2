from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.nombre
    

class Post(models.Model):
    titulo = models.CharField(max_length=50) 
    contenido = models.TextField()
    imagen = models.ImageField(upload_to='blog', blank=True, null= True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    
    def __str__(self):
        return self.titulo
    
    def mis_comentarios(self):
        return self.comentario_set.all()

class Comentario(models.Model):
    contenido = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='comentario'
        verbose_name_plural='comentarios'
    
    def __str__(self):
        return f"{self.post} {self.contenido}"
    