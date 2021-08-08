from django.contrib.auth.decorators import login_required
from django.urls import include, path

from .views import (
    FamilyGroupCreateView, FamilyGroupDeleteView, FamilyGroupListView,
    FamilyGroupUpdateView,
)


app_name = 'family_group'

urlpatterns = [

    path('list/', login_required(FamilyGroupListView.as_view()), name='list'),
    path(
        'create/', login_required(FamilyGroupCreateView.as_view()),
        name='create'
    ),
    path(
        'update/<int:pk>/', login_required(FamilyGroupUpdateView.as_view()),
        name='update'
    ),
    path(
        'delete/<int:pk>/', login_required(FamilyGroupDeleteView.as_view()),
        name='delete'
    ),
    path('person/', include('living_place.family_group.person.urls')),
]
