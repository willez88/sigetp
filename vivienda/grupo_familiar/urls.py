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
## @namespace grupo_familiar.urls
#
# Contiene las rutas de la aplicación grupo_familiar
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import (
    GrupoFamiliarList,GrupoFamiliarCreate,GrupoFamiliarUpdate,GrupoFamiliarDelete
)

urlpatterns = [

    url(r'^$', login_required(GrupoFamiliarList.as_view()), name='grupo_familiar_lista'),
    url(r'^registro/$', login_required(GrupoFamiliarCreate.as_view()), name='grupo_familiar_registro'),
    url(r'^actualizar/(?P<pk>\d+)/$', login_required(GrupoFamiliarUpdate.as_view()), name='grupo_familiar_actualizar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(GrupoFamiliarDelete.as_view()), name='grupo_familiar_eliminar'),
    url(r'^persona/', include('vivienda.grupo_familiar.persona.urls')),
]
