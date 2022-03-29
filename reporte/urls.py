from django.urls import path
from .views import reporte_usuario

urlpatterns = [
    path('reporte-usuario/', reporte_usuario, name='reporte_usuario'),
]
