from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import (
    PersonaList,
    PersonaCreate,
    PersonaUpdate,
    PersonaDelete
)

urlpatterns = [

    url(r'^$', login_required(PersonaList.as_view()), name='persona_lista'),
    url(r'^registro$', login_required(PersonaCreate.as_view()), name='persona_registro'),
    url(r'^editar/(?P<pk>\d+)$', login_required(PersonaUpdate.as_view()), name='persona_editar'),
    url(r'^borrar/(?P<pk>\d+)$', login_required(PersonaDelete.as_view()), name='persona_borrar'),
]
