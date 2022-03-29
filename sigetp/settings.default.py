"""
Django settings for sigetp project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#a#q#x4m^zb0j*-j1s(%%#=y)&1cb@n0z=*%kbnvaq!i(v5nvv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Identifica a los administradores del sistema
ADMINS = [
    ('William Páez', 'paez.william8@gmail.com'),
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'base',
    'user',
    'living_place',
    'living_place.family_group',
    'living_place.family_group.person',
    # 'reporte',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sigetp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'sigetp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    # 'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': BASE_DIR / 'db.sqlite3',
    # }

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sigetp',
        'USER': 'admin',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

# Configuración del código del lenguaje a utilizar por defecto
LANGUAGE_CODE = 'es-ve'

# Configuración para el nombre de localización por defecto
LOCALE_NAME = 'es'

# Configuración para la zona horaria por defecto
TIME_ZONE = 'America/Caracas'

# Determina si se emplea la internacionalización I18N
USE_I18N = True

# Determina si se emplea la internacionalización L10N
USE_L10N = True

# Determina si se emplea la zona horaria
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# Configuración de la url que atenderá las peticiones de los archivos estáticos
# del sistema
STATIC_URL = '/static/'

# Configuración de la raíz donde se encuentran los archivos estaticos del
# sistema (para entornos en producción)
MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'

# Configuración de los directorios en donde se encuentran los archivos
# estáticos
STATICFILES_DIRS = (
    BASE_DIR / 'static/',
    BASE_DIR / 'media/',
)

# URL de acceso al sistema
LOGIN_URL = 'user:login'

LOGIN_REDIRECT_URL = 'base:home'

LOGOUT_REDIRECT_URL = 'user:login'

# configuración que permite obtener la ruta en donde se encuentran las
# traducciones de la aplicación a otros lenguajes
LOCALE_PATHS = [
    # BASE_DIR / 'locale',
]

# Registro de mensajes al usuario
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

if DEBUG:
    # Configuración para entornos de desarrollo
    EMAIL_HOST_USER = 'email@email.com'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    # Configuración para entornos de producción
    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = 'email@email.com'
    EMAIL_HOST_PASSWORD = 'password'
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
