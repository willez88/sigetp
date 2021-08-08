from django.contrib import admin

from .models import FamilyGroup


class FamilyGroupAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo FamilyGroup al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('living_place', 'family_last_name',)
    list_filter = ('living_place',)
    list_per_page = 25
    ordering = ('living_place',)


admin.site.register(FamilyGroup, FamilyGroupAdmin)
