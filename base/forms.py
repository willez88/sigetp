from django import forms

from .fields import RifField
from .models import CommunalCouncil, Municipality, Parish, State


class CommunalCouncilAdminForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario del consejo comunal

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    def __init__(self, *args, **kwargs):
        """!
        Método que permite inicializar el formulario

        @author William Páez (paez.william8 at gmail.com)
        @param self <b>{object}</b> Objeto que instancia la clase
        @param *args <b>{tupla}</b> Tupla de valores, inicialmente vacia
        @param *kwargs <b>{dict}</b> Diccionario de datos, inicialmente vacio
        """

        super().__init__(*args, **kwargs)
        # Si se ha seleccionado un estado establece el listado de municipios y
        # elimina el atributo disable
        if 'state' in self.data and self.data['state']:
            self.fields['municipality'].widget.attrs.pop('disabled')
            self.fields['municipality'].queryset = Municipality.objects.filter(
                state=self.data['state']
            )

            # Si se ha seleccionado un municipio establece el listado de
            # parroquias y elimina el atributo disable
            if 'municipality' in self.data and self.data['municipality']:
                self.fields['parish'].widget.attrs.pop('disabled')
                self.fields['parish'].queryset = Parish.objects.filter(
                    municipality=self.data['municipality']
                )

    # Rif del consejo comunal
    rif = RifField()

    # Nombre del consejo comunal
    name = forms.CharField(
        label='Nombre del Consejo Comunal:',
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique el Nombre del RIF',
            }
        )
    )

    # Estado donde se ecnuetra ubicado el municipio
    state = forms.ModelChoiceField(
        label='Estado:', queryset=State.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip',
            'title': 'Seleccione el estado en donde se encuentra ubicada',
        })
    )

    # Municipio donde se encuentra ubicada la parroquia
    municipality = forms.ModelChoiceField(
        label='Municipio:', queryset=Municipality.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip',
            'disabled': 'true',
            'title': 'Seleccione el municipio en donde se encuentra ubicada',
        })
    )

    # Parroquia donde se encuentra ubicado el consejo comunal
    parish = forms.ModelChoiceField(
        label='Parroquia:', queryset=Parish.objects.all(),
        empty_label='Seleccione...',
        widget=forms.Select(attrs={
            'class': 'form-control select2', 'data-toggle': 'tooltip',
            'disabled': 'true',
            'title': 'Seleccione la parroquia en donde se encuentra ubicada',
        })
    )

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        """

        model = CommunalCouncil
        fields = [
            'rif', 'name', 'state', 'municipality', 'parish'
        ]
