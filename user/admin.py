from django.contrib import admin

from .forms import CommunalCouncilLevelAdminForm
from .models import CommunalCouncilLevel, Pollster, Profile


class ProfileAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Profile al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    # Mostrar los campos
    list_display = ('user', 'phone',)

    # Filtrar por campos
    list_filter = ('user__groups',)

    # Mostrar 25 registros por página
    # list_per_page = 25

    # Ordenar por usuario
    # ordering = ('consejo_comunal',)

    # Buscar por campos
    # search_fields = ('telefono', 'user',)


class CommunalCouncilLevelAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo CommunalCouncilLevel al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    form = CommunalCouncilLevelAdminForm
    change_form_template = 'user/admin/change_form.html'

    list_display = ('profile', 'communal_council',)
    # list_filter = ('communal_council',)
    # list_per_page = 25
    # ordering = ('communal_council',)


class PollsterAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Pollster al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('profile', 'communal_council_level',)
    # list_filter = ('communal',)
    # list_per_page = 25
    # ordering = ('communal',)


admin.site.register(Profile, ProfileAdmin)
admin.site.register(CommunalCouncilLevel, CommunalCouncilLevelAdmin)
admin.site.register(Pollster, PollsterAdmin)
