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
    url(r'^actualizar/(?P<pk>\d+)/$', login_required(GrupoFamiliarUpdate.as_view()), name='grupo_familiar_actualizar'),
    url(r'^eliminar/(?P<pk>\d+)/$', login_required(GrupoFamiliarDelete.as_view()), name='grupo_familiar_eliminar'),
    url(r'^persona/', include('vivienda.grupo_familiar.persona.urls')),
]
