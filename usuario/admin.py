from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import PerfilAdminForm
from .models import Perfil
from django.contrib.auth.models import User
# Register your models here.

# Se quita del registro User
admin.site.unregister(User)

class PerfilInline(admin.StackedInline):
    model = Perfil
    form = PerfilAdminForm

class PerfilAdmin(UserAdmin):
    inlines = (PerfilInline,)

admin.site.register(User, PerfilAdmin)
