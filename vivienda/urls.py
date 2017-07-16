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

    url('^$', login_required(ViviendaList.as_view()), name='vivienda_lista'),
    url(r'^registro$', login_required(ViviendaCreate.as_view()), name='vivienda_registro'),
    url(r'^editar/(?P<pk>\d+)$', login_required(ViviendaUpdate.as_view()), name='vivienda_editar'),
    url(r'^borrar/(?P<pk>\d+)$', login_required(ViviendaDelete.as_view()), name='vivienda_borrar'),
    url(r'^imagen/registro$', login_required(ImagenCreate.as_view()), name='imagen_registro'),
    url(r'^imagen$', login_required(ImagenList.as_view()), name='imagen_lista'),
    url(r'^grupo-familiar/', include('vivienda.grupo_familiar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
