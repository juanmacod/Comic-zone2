from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import Post_Form, Comentario_Form
# Create your views here.

def blog(request):
#Crear un post, ver los ultimos post, ver tus post, etc.
    posts = Post.objects.all()
    return render(request,'blog/blog.html', {'posts': posts})





# @login_required  # El decorador login_required asegura que solo los usuarios autenticados puedan acceder a esta vista
# def crear_post(request):
#     if request.method == 'POST':
#         form = Post_Form(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.autor = request.user
#             post.save()
#             form.save_m2m()  
#             return redirect('home')  
#     else:
#         form = Post_Form()
    
#     return render(request, 'blog/crear_post.html', {'form': form})




# subir noticia desde blog vvvvvvvvvvvvvvvvvvvvvvvvvvv
# para ver el formulario la url es http://localhost:8000/blog/registrar_noticia/
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
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


@login_required
def crear_comentario(request):
    if request.method == 'POST':
        form = Comentario_Form
        if form.is_valid():
           pass 



def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    return render(request,'blog/post_detail.html', {'posts': post}) 

def buscar_posts(request):
    if 'q' in request.POST:
        query = request.POST['q']
        posts = Post.objects.filter(titulo__icontains=query)
    else:
        posts = Post.objects.all()
    
    return render(request, 'blog/blog.html', {'posts': posts})