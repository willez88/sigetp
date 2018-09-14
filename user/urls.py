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
## @namespace user.urls
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
from .views import (
    CommunalCouncilLevelUpdateView, PollsterListView, PollsterFormView, PollsterUpdateView
)
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

app_name = 'user'

urlpatterns = [

    path('login/', views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('reset/password_reset/', views.PasswordResetView.as_view(template_name='user/password_reset_form.html',
        email_template_name='password_reset_email.html'),
        name='password_reset'),
    path('password_reset_done/', views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),
        name='password_reset_done'),
    path('reset/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),
        name='password_reset_complete'),
    path('password-change/', views.PasswordChangeView.as_view(template_name='user/password_change_form.html'), name='password_change'),
    path('password-change-done/', views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'), name='password_change_done'),

    path('comunal-council-level/update/<int:pk>/', login_required(CommunalCouncilLevelUpdateView.as_view()), name='communal_update'),

    path('pollster/list/', login_required(PollsterListView.as_view()), name='pollster_list'),
    path('pollster/create/', login_required(PollsterFormView.as_view()), name='pollster_create'),
    path('pollster/update/<int:pk>/', login_required(PollsterUpdateView.as_view()), name='pollster_update'),
]