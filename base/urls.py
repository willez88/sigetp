"""
Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica (SIGETP)

Copyleft (@) 2017 CENDITEL nodo Mérida
"""
## @namespace base.urls
#
# Contiene las urls del módulo base
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>

from __future__ import unicode_literals
from django.conf.urls import url
from .views import Inicio, Error403
from .ajax import *

urlpatterns = [
    url(r'^$', Inicio.as_view(), name='inicio'),
    url(r'^403/$', Error403.as_view(), name = "base_403"),
]

## URLs de peticiones AJAX
urlpatterns += [
    url(r'^ajax/actualizar-combo/?$', actualizar_combo, name='actualizar_combo'),
]
