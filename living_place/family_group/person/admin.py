from django.contrib import admin

from .models import Person


class PersonAdmin(admin.ModelAdmin):
    """!
    Clase que agrega modelo Person al panel administrativo

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    list_display = ('family_group', 'first_name', 'last_name', 'identity_card')
    list_filter = ('family_group',)
    # ordering = ('family_group',)


admin.site.register(Person, PersonAdmin)
