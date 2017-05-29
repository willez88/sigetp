from django.conf.urls import url

from .views import (
    PersonaList,
    PersonaCreate,
    PersonaUpdate,
    #GrupoFamiliarDelete
)

urlpatterns = [

    url(r'^$', PersonaList.as_view(), name='persona_lista'),
    #url(r'^(?P<pk>\d+)$', CourseDetail.as_view(), name='encuestador_detail'),
    url(r'^registro$', PersonaCreate.as_view(), name='persona_registro'),
    url(r'^editar/(?P<pk>\d+)$', PersonaUpdate.as_view(), name='persona_editar'),
    #url(r'^borrar/(?P<pk>\d+)$', GrupoFamiliarDelete.as_view(), name='grupo_familiar_borrar'),
]
