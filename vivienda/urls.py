from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from .views import (
    ViviendaList,
    ViviendaCreate,
    ViviendaUpdate,
    ViviendaDelete,
    ImagenCreate,
    ImagenList,
)

urlpatterns = [

    url(r'^$', login_required(ViviendaList.as_view()), name='vivienda_lista'),
    url(r'^registro$', ViviendaCreate.as_view(), name='vivienda_registro'),
    url(r'^editar/(?P<pk>\d+)$', ViviendaUpdate.as_view(), name='vivienda_editar'),
    url(r'^borrar/(?P<pk>\d+)$', ViviendaDelete.as_view(), name='vivienda_borrar'),
    url(r'^imagen/registro$', ImagenCreate.as_view(), name='imagen_registro'),
    url(r'^imagen$', ImagenList.as_view(), name='imagen_lista'),
    url(r'^grupo-familiar/', include('vivienda.grupo_familiar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
