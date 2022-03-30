from django.contrib import admin

from .models import FamilyGroup


class FamilyGroupAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo FamilyGroup al panel administrativo

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    list_display = ('living_place', 'family_last_name',)
    list_filter = ('living_place',)
    list_per_page = 25
    ordering = ('living_place',)


admin.site.register(FamilyGroup, FamilyGroupAdmin)
