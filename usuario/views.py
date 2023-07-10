from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from .forms import RegistroUsuarioForm
# Create your views here.

def registro_views(request):
    if request.method =='POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(reques,user)
            messages.success(request,"Registrado satisfactoriamente.")
            return HttpResponseRedirect('/crudapp/mostrar/')
        messages.error(request,"Registro invalido. Algunos datos son incorrectos")
    form = RegistroUsuarioForm()
    context = {'register_form':form}
    return render(request, "usuario/registro.html", context)
