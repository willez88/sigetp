from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import include, path, re_path
from django.views.static import serve

from .views import (
    LivingPlaceCreateView, LivingPlaceDeleteView, LivingPlaceListView,
    LivingPlaceUpdateView, PhotographCreateView, PhotographDeleteView,
    PhotographListView,
)

app_name = 'living_place'

urlpatterns = [

    path('list/', login_required(LivingPlaceListView.as_view()), name='list'),
    path(
        'create/', login_required(LivingPlaceCreateView.as_view()),
        name='create'
    ),
    path(
        'update/<int:pk>/', login_required(LivingPlaceUpdateView.as_view()),
        name='update'
    ),
    path(
        'delete/<int:pk>/', login_required(LivingPlaceDeleteView.as_view()),
        name='delete'
    ),
    path(
        'photograph/', login_required(PhotographListView.as_view()),
        name='photograph_list'
    ),
    path(
        'photograph/create/', login_required(PhotographCreateView.as_view()),
        name='photograph_create'
    ),
    path(
        'photograph/delete/<int:pk>/',
        login_required(PhotographDeleteView.as_view()),
        name='photograph_delete'
    ),
    path('family-group/', include('living_place.family_group.urls')),

    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
]
