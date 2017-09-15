from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

@staff_member_required
def reporte_usuario(request):
    reporte_usuario = []
    user = User.objects.all()
    for u in user:
        if not u.is_superuser:
            reporte_usuario.append( (u.first_name,u.last_name,u.perfil.cedula,u.email,u.perfil.telefono,u.perfil.consejo_comunal) )

    return render(request, 'reporte.reporte.usuario.template.html', {'reporte_usuario': reporte_usuario})
