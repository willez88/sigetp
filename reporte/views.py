"""
Nombre del software: SIGETP

Descripción: Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica

Nombre del licenciante y año: Fundación CENDITEL (2017)

Autores: William Páez

La Fundación Centro Nacional de Desarrollo e Investigación en Tecnologías Libres (CENDITEL),
ente adscrito al Ministerio del Poder Popular para Educación Universitaria, Ciencia y Tecnología
(MPPEUCT), concede permiso para usar, copiar, modificar y distribuir libremente y sin fines
comerciales el "Software - Registro de bienes de CENDITEL", sin garantía
alguna, preservando el reconocimiento moral de los autores y manteniendo los mismos principios
para las obras derivadas, de conformidad con los términos y condiciones de la licencia de
software de la Fundación CENDITEL.

El software es una creación intelectual necesaria para el desarrollo económico y social
de la nación, por tanto, esta licencia tiene la pretensión de preservar la libertad de
este conocimiento para que contribuya a la consolidación de la soberanía nacional.

Cada vez que copie y distribuya el "Software - Registro de bienes de CENDITEL"
debe acompañarlo de una copia de la licencia. Para más información sobre los términos y condiciones
de la licencia visite la siguiente dirección electrónica:
http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/
"""
## @namespace reporte.views
#
# Contiene las clases, atributos, métodos y/o funciones a implementar para las vistas de la aplicación reporte
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from vivienda.models import Vivienda
from vivienda.grupo_familiar.models import GrupoFamiliar
from vivienda.grupo_familiar.persona.models import Persona

# Create your views here.

@staff_member_required
def reporte_usuario(request):
    """!
    Metodo que hace el reporte de la actividad de los usuarios del sistema

    @author William Páez (wpaez at cenditel.gob.ve)
    @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
    @date 24-05-2017
    @param request <b>{object}</b> Objeto que recibe la petición
    @return Retorna los datos del usuario junto con el número de viviendas, grupos familiares y personas
    """

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
