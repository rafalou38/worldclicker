"""
Django settings for world_clicker project.

Generated by 'django-admin startproject' using Django 3.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l$s)dgtg6zd9@cuei1eusgflm(uea2=^#ps7@i^yw#f43np(34'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['rafalou38.pythonanywhere.com', 'localhost', '192.168.1.1', '0.0.0.0']


# Application definition

INSTALLED_APPS = [
    #django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


    #modules
	'django_extensions',
    'django_countries',
    'pwa',
	'crispy_forms',
	#'channels',

    #apps
    'main_app.apps.MainAppConfig',
	'users.apps.UsersConfig',

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

ROOT_URLCONF = 'world_clicker.urls'
ASGI_APPLICATION = "world_clicker.routing.application"

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'world_clicker.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = '/home/rafalou38/main_app/static'


#pwa


STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static'), ]

PWA_APP_NAME             = 'World Clicker'
PWA_APP_DESCRIPTION      = "Click for the world!"
PWA_APP_THEME_COLOR      = '#0A0302'
PWA_APP_BACKGROUND_COLOR = '#ffffff'
PWA_APP_DISPLAY          = 'standalone'
PWA_APP_SCOPE            = '/'
PWA_APP_ORIENTATION      = 'any'
PWA_APP_START_URL        = '/'
PWA_APP_ICONS            = [ { 'src': '/static/icon.png', 'sizes'          : '512x512' } ]
PWA_APP_ICONS_APPLE      = [ { 'src': '/static/icon.png', 'sizes'        : '512x512' } ]
PWA_APP_DIR              = 'ltr'
PWA_APP_LANG             = 'en-US'




CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL   = 'index'
LOGIN_URL            = 'login'
MEDIA_ROOT           = os.path.join(BASE_DIR, "media")
MEDIA_URL            = "/media/"