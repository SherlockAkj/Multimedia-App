import os
import dj_database_url 
from pathlib import Path
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-n!651_5pxd1%+y%(e3+d!w=*z9e7!$o$x5%n*q@fwe_nk!_s4*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['Multimedia-App']
CSRF_TRUSTED_ORIGINS = ['https://multimedia-app-j4x2.onrender.com']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'multimedia_app',
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

ROOT_URLCONF = 'multimedia_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'multimedia_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

import os
import sys

# Skip DB config if running collectstatic (build step)
if 'collectstatic' not in sys.argv:
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# multimedia_project/settings.py

import os # Ensure this import is at the top of your settings.py

# ... (rest of your settings.py content) ...

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
# Directory where Django will collect all static files for deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Additional directories where Django will look for static files
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'multimedia_app/static'),
]

# Media files (user-uploaded content)
# This is where Django will store uploaded files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# This is the URL prefix for media files
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = []
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# 3. Configure SECRET_KEY from environment variable
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-insecure-default-secret-key-for-local-dev-only')

# 4. Database Configuration (PostgreSQL for Render)
# Render provides a DATABASE_URL environment variable.
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3', # Default to SQLite for local development
        conn_max_age=600 # Optional: connection longevity
    )
}

# 5. Static Files Configuration for Production (WhiteNoise)
# Render serves static files directly from Django using WhiteNoise.
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add these lines for WhiteNoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 6. Media Files Configuration (Render's ephemeral filesystem)
# IMPORTANT: Render's filesystem is ephemeral. Files uploaded to MEDIA_ROOT
# will be lost when the service restarts.
# For production, you should use a cloud storage solution like Amazon S3.
# This guide keeps the local media config for simplicity, but be aware of this limitation.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# ... (rest of your settings.py content) ...

# Add this at the very end of your settings.py for WhiteNoise middleware
MIDDLEWARE = [
    # ... other middleware ...
    'whitenoise.middleware.WhiteNoiseMiddleware', # Add this line
    # ... other middleware ...
]