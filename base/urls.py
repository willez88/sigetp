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
from . import views
from .ajax import *

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
]

## URLs de peticiones AJAX
urlpatterns += [
    #url(r'^ajax/get-data-rif/?$', get_data_rif, name='get_data_rif'),
    #url(r'^ajax/validar-rif-seniat/?$', validar_rif_seniat, name='validar_rif_seniat'),
    url(r'^ajax/actualizar-combo/?$', actualizar_combo, name='actualizar_combo'),
    #url(r'^ajax/eliminar-registro/$', eliminar_registro, name="eliminar_registro"),
    #url(r'^ajax/cargar-combo/?$', cargar_combo, name='cargar_combo'),
    #url(r'^ajax/anho-registro/$', anho_registro, name='anho_registro'),
    #url(r'^ajax/cliente-data$', client_data ,name="ajax_cliente_data"),
    #url(r'^ajax/count-model$', count_model ,name="ajax_count_model"),
    #url(r'^datatable-espanol$', datatable_json ,name="datatable_espanol"),
]
