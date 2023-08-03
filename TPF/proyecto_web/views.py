from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
#pagina de inicio solamente la presentacion del blog 
    return render(request,'proyecto_web/home.html')




def login(request):

    return render(request,'proyecto_web/login.html')

def registro(request):

    return render(request,'proyecto_web/registro.html')

def contacto(request):
#contacto a "nosotros"
    return render(request,'proyecto_web/contacto.html')

