"""
Django settings for sigetp project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#a#q#x4m^zb0j*-j1s(%%#=y)&1cb@n0z=*%kbnvaq!i(v5nvv'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


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
    'encuestador',
    'encuestador.vivienda',
    'encuestador.vivienda.grupo_familiar',
    'encuestador.vivienda.grupo_familiar.persona',
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

## Directorio en donde se encuentran las plantillas del módulo base
BASE_TEMPLATES = os.path.join(BASE_DIR, "base/templates")
ENCUESTADOR_TEMPLATES = os.path.join(BASE_DIR, "encuestador/templates")
VIVIENDA_TEMPLATES = os.path.join(BASE_DIR, "encuestador/vivienda/templates")
GRUPO_FAMILIAR_TEMPLATES = os.path.join(BASE_DIR, "encuestador/vivienda/grupo_familiar/templates")
PERSONA_TEMPLATES = os.path.join(BASE_DIR, "encuestador/vivienda/grupo_familiar/persona/templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_TEMPLATES, ENCUESTADOR_TEMPLATES, GRUPO_FAMILIAR_TEMPLATES, PERSONA_TEMPLATES],
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
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sigetp',
        'USER': 'postgres',
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

## Configuración del código del lenguaje a utilizar por defecto
LANGUAGE_CODE = 'es-ve'

## Configuración para el nombre de localización por defecto
LOCALE_NAME = 'es'

## Configuración para la zona horaria por defecto
TIME_ZONE = 'America/Caracas'

## Determina si se emplea la internacionalización I18N
USE_I18N = True

## Determina si se emplea la internacionalización L10N
USE_L10N = True

## Determina si se emplea la zona horaria
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

## Configuración de la raíz donde se encuentran los archivos estaticos del sistema (para entornos en producción)
STATIC_ROOT = ''

## Configuración de la url que atenderá las peticiones de los archivos estáticos del sistema
STATIC_URL = '/static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = ''
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

## Configuración de los directorios en donde se encuentran los archivos estáticos
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
    #os.path.join(BASE_DIR, 'media/'),
)

## URL de acceso al sistema
LOGIN_URL = "/login"

## URL de salida del sistema
LOGOUT_URL = "/logout"

## configuración que permite obtener la ruta en donde se encuentran las traducciones de la aplicación a otros lenguajes
LOCALE_PATHS = [
    #os.path.join(BASE_DIR, 'locale'),
]

## Registro de mensajes al usuario
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

# Configuración de variables para el envío de correo electrónico
## Nombre del Servidor de correo SMTP
#EMAIL_HOST = 'localhost'
## Puerto del Servidor de correo SMTP
#EMAIL_PORT = 25
## Dirección de correo electrónico de quien envía
#EMAIL_FROM = 'sigesic@cenditel.gob.ve'

