"""
Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica (SIGETP)

Copyleft (@) 2017 CENDITEL nodo Mérida
"""
## @namespace base.views
#
# Contiene las clases, atributos, métodos y/o funciones a implementar para las vistas del módulo base
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @copyright <a href='http://www.gnu.org/licenses/gpl-3.0.html'>GNU Public License versión 3 (GPLv3)</a>

from django.shortcuts import render
from django.views.generic import TemplateView

__licence__ = "GNU Public License v2"
__revision__ = ""
__docstring__ = "DoxyGen"


class Inicio(TemplateView):
    template_name = "base.template.html"

class Error403(TemplateView):
    template_name = "base.403.html"
