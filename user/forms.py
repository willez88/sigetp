from base.fields import IdentityCardField, PhoneField
from base.models import Municipality, Parish, State
from django import forms
from django.contrib.auth.models import User
from django.core import validators

from .models import CommunalCouncilLevel, Profile


class CommunalCouncilLevelAdminForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario del perfil usado en el
    panel administrativo

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

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

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        model = User
        fields = '__all__'


class ProfileForm(forms.ModelForm):
    """!
    Clase que contiene los campos del formulario de perfil del usuario

    @author William Páez (paez.william8 at gmail.com)
    @copyright <a href='​http://www.gnu.org/licenses/gpl-2.0.html'>
        GNU Public License versión 2 (GPLv2)</a>
    """

    # Username para identificar al usuario, en este caso se usa la cédula
    username = IdentityCardField(
        validators=[
            validators.RegexValidator(
                r'^[VE][\d]{8}$',
                'Introduzca un número de cédula válido. Solo se permiten \
                    números y una longitud de 8 carácteres. Se agregan ceros \
                    (0) si la longitud es de 7 o menos caracteres.'
            ),
        ]
    )

    # Nombres del usuario
    first_name = forms.CharField(
        label='Nombres:', max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique los Nombres',
            }
        )
    )

    # Apellidos del usuario
    last_name = forms.CharField(
        label='Apellidos:', max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique los Apellidos',
            }
        )
    )

    # Correo del usuario
    email = forms.EmailField(
        label='Correo Electrónico:', max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control input-sm email-mask',
                'data-toggle': 'tooltip',
                'title': 'Indique el correo electrónico de contacto'
            }
        )
    )

    # Teléfono del usuario
    phone = PhoneField(
        validators=[
            validators.RegexValidator(
                r'^\+\d{2}-\d{3}-\d{7}$',
                'Número telefónico inválido. Solo se permiten números.'
            ),
        ]
    )

    # Clave de acceso del usuario
    password = forms.CharField(
        label='Contraseña:', max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique una contraseña de aceso al sistema'
            }
        )
    )

    # Confirmación de clave de acceso del usuario
    confirm_password = forms.CharField(
        label='Confirmar Contraseña:', max_length=128,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'title': 'Indique nuevamente la contraseña de aceso al sistema'
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email):
            raise forms.ValidationError('El correo ya esta registrado')
        return email

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data['confirm_password']
        password = self.cleaned_data.get('password')
        if password != confirm_password:
            raise forms.ValidationError('La contraseña no es la misma')
        return confirm_password

    # class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez (paez.william8 at gmail.com)
        """

        # model = User
        # exclude = ['profile','date_joined']


class CommunalCouncilLevelUpdateForm(ProfileForm):

    def __init__(self, *args, **kwargs):
        super(CommunalCouncilLevelUpdateForm, self).__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['confirm_password'].required = False
        self.fields['password'].widget.attrs['disabled'] = True
        self.fields['confirm_password'].widget.attrs['disabled'] = True

    communal_council = forms.CharField(
        label='Consejo Comunal:',
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'readonly': 'true', 'style': 'width:100%',
                'title': 'Consejo Comunal que tiene asignado',
            }
        ), required=False
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError('El correo ya esta registrado')
        return email

    def clean_confirm_password(self):
        pass

    class Meta:
        model = Profile
        fields = [
            'username', 'first_name', 'last_name', 'email', 'phone'
        ]


class PollsterForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        if CommunalCouncilLevel.objects.filter(profile=user.profile):
            communal_council_level = CommunalCouncilLevel.objects.get(
                profile=user.profile
            )
            self.fields[
                'communal_council'
            ].initial = communal_council_level.communal_council

    communal_council = forms.CharField(
        label='Consejo Comunal:',
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'readonly': 'true', 'style': 'width:100%',
                'title': 'Consejo Comunal que tiene asignado',
            }
        ), required=False
    )

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        model = User
        fields = [
            'username', 'first_name', 'last_name', 'email', 'phone',
            'password', 'confirm_password'
        ]


class PollsterUpdateForm(ProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False
        self.fields['confirm_password'].required = False
        self.fields['password'].widget.attrs['disabled'] = True
        self.fields['confirm_password'].widget.attrs['disabled'] = True

    communal_council = forms.CharField(
        label='Consejo Comunal:',
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control input-sm', 'data-toggle': 'tooltip',
                'readonly': 'true', 'style': 'width:100%',
                'title': 'Consejo Comunal que tiene asignado',
            }
        ), required=False
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError('El correo ya esta registrado')
        return email

    def clean_confirm_password(self):
        pass

    class Meta:
        """!
        Meta clase del formulario que establece algunas propiedades

        @author William Páez <wpaez@cenditel.gob.ve>
        """

        model = Profile
        fields = [
            'username', 'first_name', 'last_name', 'email', 'phone'
        ]
