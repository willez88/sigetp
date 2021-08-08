from django.contrib.auth.decorators import login_required
from django.urls import path

from .ajax import ComboUpdateView
from .views import Error403TemplateView, HomeTemplateView

app_name = 'base'

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('error-403/', Error403TemplateView.as_view(), name='error_403'),
    path(
        'ajax/combo-update/', login_required(ComboUpdateView.as_view()),
        name='combo_update'
    ),
]
