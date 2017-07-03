from django.contrib import admin
from .forms import PerfilAdminForm
from .models import Perfil
# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    form = PerfilAdminForm
    list_display = ('user','cedula','telefono')

admin.site.register(Perfil, PerfilAdmin)
