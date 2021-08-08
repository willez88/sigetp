from django.contrib import admin

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Person al panel administrativo

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    list_display = ('family_group', 'first_name', 'last_name', 'identity_card')
    list_filter = ('family_group',)
    # ordering = ('family_group',)


admin.site.register(Person, PersonAdmin)
