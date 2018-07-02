"""
Nombre del software: SIGETP

Descripción: Sistema Integrado de Información y Documentación Geoestadística y Tecnopolítica

Nombre del licenciante y año: Fundación CIDA (2017)

Autores: William Páez

La Fundación Centro Nacional de Desarrollo e Investigación en Tecnologías Libres (CENDITEL),
ente adscrito al Ministerio del Poder Popular para Educación Universitaria, Ciencia y Tecnología
(MPPEUCT), concede permiso para usar, copiar, modificar y distribuir libremente y sin fines
comerciales el "Software - Registro de bienes de CENDITEL", sin garantía
alguna, preservando el reconocimiento moral de los autores y manteniendo los mismos principios
para las obras derivadas, de conformidad con los términos y condiciones de la licencia de
software de la Fundación CENDITEL.

El software es una creación intelectual necesaria para el desarrollo económico y social
de la nación, por tanto, esta licencia tiene la pretensión de preservar la libertad de
este conocimiento para que contribuya a la consolidación de la soberanía nacional.

Cada vez que copie y distribuya el "Software - Registro de bienes de CENDITEL"
debe acompañarlo de una copia de la licencia. Para más información sobre los términos y condiciones
de la licencia visite la siguiente dirección electrónica:
http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/
"""
## @namespace usuario.urls
#
# Contiene las rutas de la aplicación usuario
# @author William Páez (wpaez at cenditel.gob.ve)
# @author <a href='http://www.cenditel.gob.ve'>Centro Nacional de Desarrollo e Investigación en Tecnologías Libres
# (CENDITEL) nodo Mérida - Venezuela</a>
# @author <a href='www.cida.gob.ve/'>Centro de Investigaciones de Astronomía "Francisco J. Duarte"</a>
# @copyright <a href='http://conocimientolibre.cenditel.gob.ve/licencia-de-software-v-1-3/'>Licencia de Software CENDITEL versión 1.2</a>
# @date 24-05-2017
# @version 1.0

from django.urls import path, include
from .views import CommunalUpdateView, PollsterListView, PollsterCreateView, PollsterUpdateView, PollsterStatusUpdateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

app_name = 'usuario'

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='usuario/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('reset/password_reset/', auth_views.PasswordResetView.as_view(template_name='usuario/password_reset_form.html',
        email_template_name='password_reset_email.html'),
        name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='usuario/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='usuario/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='usuario/password_reset_complete.html'),
        name='password_reset_complete'),
    path('cambiar-clave/', auth_views.PasswordChangeView.as_view(template_name='usuario/password_change_form.html'), name='password_change'),
    path('cambiar-clave-hecho/', auth_views.PasswordChangeDoneView.as_view(template_name='usuario/password_change_done.html'), name='password_change_done'),

    path('comunal/actualizar/<int:pk>/', login_required(CommunalUpdateView.as_view()), name='communal_update'),

    path('encuestador/listar/', login_required(PollsterListView.as_view()), name='pollster_list'),
    path('encuestador/registrar/', login_required(PollsterCreateView.as_view()), name='pollster_create'),
    path('encuestador/actualizar/<int:pk>/', login_required(PollsterUpdateView.as_view()), name='pollster_update'),
    path('encuestador/estatus/<int:pk>/', login_required(PollsterStatusUpdateView.as_view()), name='pollster_status_update'),
]
