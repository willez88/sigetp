from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect
from django.core import urlresolvers
from django.contrib.auth.models import User
from datetime import datetime
from .forms import AutenticarForm

# Create your views here.

def acceso(request):

    form = AutenticarForm()

    if request.method == "POST":
        form = AutenticarForm(data=request.POST)

        if form.is_valid():
            usuario = request.POST['usuario']
            clave = str(request.POST['clave'])

            usuario_sistema = authenticate(username=usuario, password=clave)

            if usuario is not None:
                login(request, usuario_sistema)
                usr = User.objects.get(username=usuario)
                usr.last_login = datetime.now()
                usr.save()

            return HttpResponseRedirect(urlresolvers.reverse("inicio"))

    return render(request, 'usuario.acceso.html', {'form':form})

def salir(request):
    user = request.user
    if user.is_authenticated():
        logout(request)

    return HttpResponseRedirect(urlresolvers.reverse("inicio"))
