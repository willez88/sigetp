from django.conf.urls import url
from .views import reporte_usuario

urlpatterns = [
    url(r'^reporte-usuario/$', reporte_usuario, name='reporte_usuario'),
]
