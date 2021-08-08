from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import (
    PersonCreateView, PersonDeleteView, PersonListView,
    PersonReportTemplateView, PersonUpdateView,
)

app_name = 'person'

urlpatterns = [

    path('list/', login_required(PersonListView.as_view()), name='list'),
    path('create/', login_required(PersonCreateView.as_view()), name='create'),
    path(
        'update/<int:pk>/', login_required(PersonUpdateView.as_view()),
        name='update'
    ),
    path(
        'delete/<int:pk>/', login_required(PersonDeleteView.as_view()),
        name='delete'
    ),
    path(
        'report/', login_required(PersonReportTemplateView.as_view()),
        name='report'
    )
]
