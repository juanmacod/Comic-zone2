from django.shortcuts import render, redirect,get_object_or_404
from .models import Post, Comentario
from django.contrib.auth.decorators import login_required
from .forms import Post_Form, Comentario_Form
from django.views.generic.edit import DeleteView, UpdateView

# Create your views here.

def blog(request):
#Crear un post, ver los ultimos post, ver tus post, etc.
    posts = Post.objects.all()
    return render(request,'blog/blog.html', {'posts': posts})


# subir noticia desde blog vvvvvvvvvvvvvvvvvvvvvvvvvvv
# para ver el formulario la url es http://localhost:8000/blog/registrar_noticia/
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, UpdateView #para modificar los comentarios
from django.urls import reverse_lazy

class CrearNoticia(LoginRequiredMixin, CreateView):
	model = Post
	form_class = Post_Form
	template_name = 'noticias/registrar_noticia.html'
	success_url = reverse_lazy('blog')
	
	def form_valid(self, form):
		noticia = form.save(commit=False)
		noticia.autor = self.request.user
		return super(CrearNoticia, self).form_valid(form)


#def post_detail(request, post_id):
#    post = Post.objects.get(id=post_id)
#
#    return render(request,'blog/post_detail.html', {'posts': post}) 
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        comentario_form = Comentario_Form(request.POST)
        if comentario_form.is_valid():
            comentario = comentario_form.save(commit=False)
            comentario.autor = request.user
            comentario.post = post
            comentario.save()
            return redirect('post_detail', post_id=post.id)
    else:
        comentario_form = Comentario_Form()

    return render(request, 'blog/post_detail.html', {'post': post, 'comentario_form': comentario_form})

def buscar_posts(request):
    if 'q' in request.POST:
        query = request.POST['q']
        posts = Post.objects.filter(titulo__icontains=query)
    else:
        posts = Post.objects.all()
    
    return render(request, 'blog/blog.html', {'posts': posts})

@login_required
def comentar_post(request):
    if request.method == 'POST':
        comentario_texto = request.POST.get('comentario', None)
        post_id = request.POST.get('id', None)
        user = request.user
        post = get_object_or_404(Post, pk=post_id)
        
        comentario = Comentario.objects.create(usuario=user, post=post, contenido=comentario_texto)
        
        return redirect(reverse_lazy('post_detail', kwargs={'post_id': post_id}))
    else:
        return redirect('blog') 

from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils.decorators import method_decorator


class Borrar_comentario(DeleteView):
    model = Comentario
    template_name = "comentarios/borrar_comentario.html"

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'post_id': self.object.post.id})
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.autor != self.request.user:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


class Modificar_comentario(UpdateView):
    model = Comentario
    form_class = Comentario_Form
    template_name = 'comentarios/modificar_comentario.html'

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'post_id': self.object.post.id})
    
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.autor != self.request.user:
            raise Http404
        return super().dispatch(request, *args, **kwargs)


