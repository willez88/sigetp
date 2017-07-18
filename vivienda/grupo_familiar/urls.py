from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from .views import (
    GrupoFamiliarList,
    GrupoFamiliarCreate,
    GrupoFamiliarUpdate,
    GrupoFamiliarDelete
)

urlpatterns = [

    url(r'^$', login_required(GrupoFamiliarList.as_view()), name='grupo_familiar_lista'),
    url(r'^registro/$', login_required(GrupoFamiliarCreate.as_view()), name='grupo_familiar_registro'),
    url(r'^editar/(?P<pk>\d+)/$', login_required(GrupoFamiliarUpdate.as_view()), name='grupo_familiar_editar'),
    url(r'^borrar/(?P<pk>\d+)/$', login_required(GrupoFamiliarDelete.as_view()), name='grupo_familiar_borrar'),
    url(r'^persona/', include('vivienda.grupo_familiar.persona.urls')),
]
