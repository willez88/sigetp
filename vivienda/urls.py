"""
Nombre del software: SIGETP

Descripción: Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica

Nombre del licenciante y año: Fundación CIDA (2017)

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
## @namespace vivienda.urls
#
# Contiene las rutas de la aplicación vivienda
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from .views import (
    ViviendaList,ViviendaCreate,ViviendaUpdate,ViviendaDelete,ImagenCreate,
    ImagenList,ImagenDelete,
)

urlpatterns = [

    path('', login_required(ViviendaList.as_view()), name='vivienda_lista'),
    path('registro/', login_required(ViviendaCreate.as_view()), name='vivienda_registro'),
    path('actualizar/<int:pk>/', login_required(ViviendaUpdate.as_view()), name='vivienda_actualizar'),
    path('eliminar/<int:pk>/', login_required(ViviendaDelete.as_view()), name='vivienda_eliminar'),
    path('imagen/registro/', login_required(ImagenCreate.as_view()), name='imagen_registro'),
    path('imagen/', login_required(ImagenList.as_view()), name='imagen_lista'),
    path('imagen/eliminar/<int:pk>/', login_required(ImagenDelete.as_view()), name='imagen_eliminar'),
    path('grupo-familiar/', include('vivienda.grupo_familiar.urls')),
]
