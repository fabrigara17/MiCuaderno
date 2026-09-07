"""
Configuración de Django para el proyecto MiCuaderno (libreta).

Referencia oficial: https://docs.djangoproject.com/en/5.2/topics/settings/
"""

import os
from pathlib import Path

from dotenv import load_dotenv

# BASE_DIR apunta a la carpeta MiCuaderno/ (raíz del proyecto)
BASE_DIR = Path(__file__).resolve().parent.parent

# Carga las variables definidas en el archivo .env (si existe) al entorno,
# para que los os.environ.get() de abajo las puedan leer.
# Referencia: https://pypi.org/project/python-dotenv/
load_dotenv(BASE_DIR / '.env')

# --------------------------------------------------------------------------
# SEGURIDAD
# --------------------------------------------------------------------------
# En desarrollo podés dejar esta clave, pero para producción SIEMPRE
# defínila como variable de entorno y nunca la subas al repositorio.
# Referencia: https://docs.djangoproject.com/en/5.2/ref/settings/#secret-key
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-CAMBIAR-ESTA-CLAVE-ANTES-DE-PRODUCCION'
)

# DEBUG en True solo para desarrollo local. En producción: False.
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# --------------------------------------------------------------------------
# APPS
# --------------------------------------------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Apps propias del proyecto
    'usuarios',
    'academico',
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

ROOT_URLCONF = 'libreta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Carpeta de templates globales (base.html, etc.)
        'DIRS': [BASE_DIR / 'templates'],
        # APP_DIRS=True hace que Django también busque en <app>/templates/
        # de cada app instalada (necesario para registration/login.html)
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'libreta.wsgi.application'

# --------------------------------------------------------------------------
# BASE DE DATOS (PostgreSQL)
# Referencia: https://docs.djangoproject.com/en/5.2/ref/databases/#postgresql-notes
# --------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'libreta_db'),
        'USER': os.environ.get('DB_USER', 'libreta_user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'tu_password_segura'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

# --------------------------------------------------------------------------
# MODELO DE USUARIO CUSTOM
# Referencia: https://docs.djangoproject.com/en/5.2/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
# --------------------------------------------------------------------------
AUTH_USER_MODEL = 'usuarios.Usuario'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --------------------------------------------------------------------------
# LOGIN / LOGOUT
# Referencia: https://docs.djangoproject.com/en/5.2/topics/auth/default/#django.contrib.auth.views.LoginView
# --------------------------------------------------------------------------
LOGIN_URL = 'login'                 # nombre de la url a la que redirige @login_required
LOGIN_REDIRECT_URL = 'home'         # a dónde va el usuario tras loguearse
LOGOUT_REDIRECT_URL = 'login'       # a dónde va tras cerrar sesión

# --------------------------------------------------------------------------
# LOCALIZACIÓN
# --------------------------------------------------------------------------
LANGUAGE_CODE = 'es-ar'
TIME_ZONE = 'America/Argentina/Buenos_Aires'
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------------------------
# ARCHIVOS ESTÁTICOS
# Referencia: https://docs.djangoproject.com/en/5.2/howto/static-files/
# --------------------------------------------------------------------------
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
