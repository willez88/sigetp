from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from vivienda.models import Vivienda
from vivienda.grupo_familiar.models import GrupoFamiliar
from vivienda.grupo_familiar.persona.models import Persona

# Create your views here.

@staff_member_required
def reporte_usuario(request):
    reporte_usuario = []
    user = User.objects.all()
    for u in user:
        num_persona = 0
        num_grupo_familiar = 0
        num_vivienda = 0
        if not u.is_superuser:
            if Persona.objects.filter(grupo_familiar__vivienda__user=u):
                num_persona = Persona.objects.filter(grupo_familiar__vivienda__user=u).count()

            if GrupoFamiliar.objects.filter(vivienda__user=u):
                num_grupo_familiar = GrupoFamiliar.objects.filter(vivienda__user=u).count()

            if Vivienda.objects.filter(user=u):
                num_vivienda = Vivienda.objects.filter(user=u).count()

            reporte_usuario.append( (u.username,u.first_name,u.last_name,u.perfil.cedula,u.email,u.perfil.telefono,u.perfil.consejo_comunal,num_persona,num_grupo_familiar,num_vivienda) )

    return render(request, 'reporte.reporte.usuario.template.html', {'reporte_usuario': reporte_usuario})
