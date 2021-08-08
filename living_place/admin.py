from django.contrib import admin

from .models import LivingPlace, Photograph


class LivingPlaceAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo LivingPlace al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('user', 'communal_council',)
    list_filter = ('user', 'communal_council',)
    # list_per_page = 25
    ordering = ('communal_council',)


class PhotographAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Photograph al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('living_place', 'picture')
    list_filter = ('living_place',)
    # list_per_page = 25
    ordering = ('living_place',)


admin.site.register(LivingPlace, LivingPlaceAdmin)
admin.site.register(Photograph, PhotographAdmin)
