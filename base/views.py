from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    """!
    Clase para mostrar la página de inicio del sistema

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    template_name = 'base/base.html'


class Error403TemplateView(TemplateView):
    """!
    Clase para mostrar la página de error de permisos

    @author William Páez <wpaez@cenditel.gob.ve>
    @copyright <a href='https://tinyurl.com/y3tfnema'>
        Licencia de Software CENDITEL versión 1.2</a>
    """

    template_name = 'base/error.403.html'
