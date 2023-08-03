from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
# Create your views here.

class VRegistro(View):


    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registro/registro.html',{'form':form} )

    def post(self, request):
        form = UserCreationForm(request.POST)
        
        if form.is_valid(): #Si el registro fue exitoso nos lleva al home

            usuario = form.save()

            login(request, usuario)
            return redirect('home')

        else: 
            for msg in form.error_messages: #por cada mensaje de error 
                messages.error(request, form.error_messages[msg])#se supone que lo tendria que mostrar con esto
        return render(request, 'registro/registro.html',{'form':form} )#y tiene que mantenerse en la pagina actual



def cerrar_sesion(request):
    logout(request)


    return redirect('home')

def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            usuario=authenticate(username=nombre_usuario, password=contraseña)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request, 'usuario o contraseña invalidos')
        else:
            messages.error(request, 'usuario o contraseña invalidos')
    form=AuthenticationForm()
    return render(request, 'login/login.html',{'form':form} )