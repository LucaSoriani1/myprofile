"""
Django settings for myprofile project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
if os.environ.get('DEBUG') == 'True':
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    CORS_ORIGIN_ALLOW_ALL = True
else:
    DEBUG = False
    ALLOWED_HOSTS = ['www.lucasoriani.com', 'lucasoriani.com', '181.215.68.32', 'localhost', '127.0.0.1']
    CORS_ORIGIN_WHITELIST = (
        'https://www.lucasoriani.com',
        'https://lucasoriani.com'
    )
    CSRF_TRUSTED_ORIGINS=['https://*.lucasoriani.com']


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_profile',
    'corsheaders',
    'django_dump_load_utf8',
]

MIDDLEWARE = [
    'csp.middleware.CSPMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "django_permissions_policy.PermissionsPolicyMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'myprofile.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'myprofile.context_processors.project_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'myprofile.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME"),
        'USER': os.environ.get('POSTGRESS_USER'),
        'PASSWORD': os.environ.get('POSTRGESS_PASSWORD'),
        'HOST': os.environ.get('POSTRGESS_HOST'),
        'PORT': os.environ.get('POSTRGESS_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'it-it'

TIME_ZONE = 'CET'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DEFAULT_FROM_EMAIL = os.environ.get("EMAIL_HOST_USER")
SERVER_EMAIL = os.environ.get("EMAIL_HOST_USER")
EMAIL_BACKEND=os.environ.get('EMAIL_BACKEND')
EMAIL_HOST=os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER=os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD=os.environ.get("EMAIL_HOST_PASSWORD")
EMAIL_PORT=os.environ.get("EMAIL_PORT")
EMAIL_USE_TLS = bool(os.environ.get("EMAIL_USE_TLS"))

if not DEBUG:
    CSRF_COOKIE_HTTPONLY = True
    SESSION_COOKIE_NAME = '__Secure-sessionid'
    CSRF_COOKIE_NAME = '__Secure-csrftoken'
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    SECURE_HSTS_SECONDS = 2592000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    PERMISSIONS_POLICY = {
        "accelerometer": [],
        "ambient-light-sensor": [],
        "autoplay": [],
        "camera": [],
        "display-capture": [],
        "document-domain": [],
        "encrypted-media": [],
        "fullscreen": [],
        "geolocation": [],
        "gyroscope": [],
        "interest-cohort": [],
        "magnetometer": [],
        "microphone": [],
        "midi": [],
        "payment": [],
        "usb": [],
    }





# default source as self
CSP_DEFAULT_SRC = ("'self'", )

# style from our domain and bootstrapcdn
CSP_STYLE_SRC = ("'self'",
    "cdnjs.cloudflare.com",
    "fonts.googleapis.com",
    "'unsafe-inline'",)

# scripts from our domain and other domains
CSP_SCRIPT_SRC = ("'self'",
    "cdnjs.cloudflare.com",
    "cdn.jsdelivr.net",
    "'unsafe-inline'",)

# images from our domain and other domains
CSP_IMG_SRC = ("'self'")

# loading manifest, workers, frames, etc
CSP_FONT_SRC = ("'self'", )
CSP_CONNECT_SRC = ("'self'",
    "www.google-analytics.com" )
CSP_OBJECT_SRC = ("'self'", )
CSP_BASE_URI = ("'self'", )
CSP_FRAME_ANCESTORS = ("'self'", )
CSP_FORM_ACTION = ("'self'", )
CSP_INCLUDE_NONCE_IN = ('script-src', )
CSP_MANIFEST_SRC = ("'self'", )
CSP_WORKER_SRC = ("'self'", )
CSP_MEDIA_SRC = ("'self'", )

SECURE_BROWSER_XSS_FILTER = True