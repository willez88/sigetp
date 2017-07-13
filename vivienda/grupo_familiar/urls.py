from django.conf.urls import url, include

from .views import (
    GrupoFamiliarList,
    GrupoFamiliarCreate,
    GrupoFamiliarUpdate,
    GrupoFamiliarDelete
)

urlpatterns = [

    url(r'^$', GrupoFamiliarList.as_view(), name='grupo_familiar_lista'),
    #url(r'^(?P<pk>\d+)$', CourseDetail.as_view(), name='encuestador_detail'),
    url(r'^registro$', GrupoFamiliarCreate.as_view(), name='grupo_familiar_registro'),
    url(r'^editar/(?P<pk>\d+)$', GrupoFamiliarUpdate.as_view(), name='grupo_familiar_editar'),
    url(r'^borrar/(?P<pk>\d+)$', GrupoFamiliarDelete.as_view(), name='grupo_familiar_borrar'),
    url(r'^persona/', include('vivienda.grupo_familiar.persona.urls')),
]
