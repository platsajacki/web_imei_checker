from os import getenv
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv('SECRET_KEY')

DEBUG = getenv('DEBUG') == 'True'

ALLOWED_HOSTS = getenv('ALLOWED_HOSTS', 'localhost, 127.0.0.1').split(', ')

CSRF_TRUSTED_ORIGINS = getenv(
    'CSRF_TRUSTED_ORIGINS',
    'https://127.0.0.1, https://localhost, https://www.127.0.0.1, https://www.localhost',
).split(', ')


# Application definition
django_apps = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
third_party_apps = [
    'drf_yasg',
    'rest_framework',
    'rest_framework_api_key',
]
local_apps = [
    'apps.imei',
    'apps.telegram',
]
INSTALLED_APPS = django_apps + third_party_apps + local_apps

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': getenv('ENGINE', 'django.db.backends.postgresql'),
        'NAME': getenv('POSTGRES_DB', 'django'),
        'USER': getenv('POSTGRES_USER', 'django'),
        'PASSWORD': getenv('POSTGRES_PASSWORD', 'django'),
        'HOST': getenv('DB_HOST', 'localhost'),
        'PORT': getenv('DB_PORT', '5432'),
    }
}


# Password validation
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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework_api_key.permissions.HasAPIKey',
    ]
}

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {'Api-Key': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'}},
}

# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
