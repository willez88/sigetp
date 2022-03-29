from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from living_place.models import LivingPlace
from living_place.family_group.models import FamilyGroup
from living_place.family_group.person.models import Person


@staff_member_required
def reporte_usuario(request):
    """!
    Metodo que hace el reporte de la actividad de los usuarios del sistema

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    @param request <b>{object}</b> Objeto que recibe la petición
    @return Retorna los datos del usuario junto con el número de viviendas,
        grupos familiares y personas
    """

    reporte_usuario = []
    user = User.objects.all()
    for u in user:
        num_person = 0
        num_family_group = 0
        num_living_place = 0
        if not u.is_superuser:
            if Person.objects.filter(grupo_familiar__vivienda__user=u):
                num_person = Person.objects.filter(
                    grupo_familiar__vivienda__user=u
                ).count()

            if FamilyGroup.objects.filter(vivienda__user=u):
                num_family_group = FamilyGroup.objects.filter(
                    vivienda__user=u
                ).count()

            if LivingPlace.objects.filter(user=u):
                num_living_place = LivingPlace.objects.filter(user=u).count()

            reporte_usuario.append(
                (
                    u.username,
                    u.first_name,
                    u.last_name,
                    u.perfil.cedula,
                    u.email,
                    u.perfil.telefono,
                    u.perfil.consejo_comunal,
                    num_person,
                    num_family_group,
                    num_living_place
                )
            )

    return render(
        request, 'reporte.reporte.usuario.template.html',
        {'reporte_usuario': reporte_usuario}
    )
