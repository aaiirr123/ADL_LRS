# Django settings for adl_lrs project.
import os
from os.path import dirname, abspath

ALLOWED_HOSTS = ['*']

# Root of LRS
SETTINGS_DIR = dirname(abspath(__file__))
PROJECT_ROOT = dirname(dirname(SETTINGS_DIR))

# Helper function to parse boolean environment variables
def get_bool_env(var_name, default='False'):
    return os.environ.get(var_name, default).lower() in ('true', '1', 't', 'yes')

# If you want to debug
DEBUG = get_bool_env('DEBUG', 'False')

# Set these email values to send the reset password link
# If you do not want this functionality just comment out the
# Forgot Password? link in templates/registration/login.html
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_PORT = int(os.environ.get('EMAIL_PORT', '25'))
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_USE_SSL = get_bool_env('EMAIL_USE_SSL', 'False')
EMAIL_USE_TLS = get_bool_env('EMAIL_USE_TLS', 'False')

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

# Google reCAPTCHA Config
#
# Using reCAPTCHA currently requires a Google API key, which is free.
USE_GOOGLE_RECAPTCHA = get_bool_env('USE_GOOGLE_RECAPTCHA', 'False')
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY', '')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY', '')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'lrs'),
        'USER': os.environ.get('DB_USER', 'lrs'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'lrs'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': int(os.environ.get('DB_PORT', '5432')),
    }
}

# Local time zone for this installation
TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')

# Language code for this installation
LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en-us')

# The ID, as an integer, of the current site in the django_site database table
SITE_ID = int(os.environ.get('SITE_ID', '1'))

# Internationalization settings
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Set this to True if you would like to utilize the webhooks functionality
USE_HOOKS = get_bool_env('USE_HOOKS', 'False')

# Newer versions of Django recommend specifying a default auto field here
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Absolute filesystem path to the directory that will hold user-uploaded files
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# Paths for xAPI media
AGENT_PROFILE_UPLOAD_TO = "agent_profile"
ACTIVITY_STATE_UPLOAD_TO = "activity_state"
ACTIVITY_PROFILE_UPLOAD_TO = "activity_profile"
STATEMENT_ATTACHMENT_UPLOAD_TO = "attachment_payloads"

# URL that handles the media served from MEDIA_ROOT
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to
STATIC_ROOT = '/opt/lrs/ADL_LRS/adl_lrs/static/'

# URL prefix for static files
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Add paths here
)

# Current xAPI version
XAPI_VERSION = '2.0.0'
XAPI_VERSIONS = ['1.0.0', '1.0.1', '1.0.2', '1.0.3', XAPI_VERSION]

# Where to be redirected after logging in
LOGIN_REDIRECT_URL = '/me'

# Me view has a tab of user's statements
STMTS_PER_PAGE = int(os.environ.get('STMTS_PER_PAGE', '10'))

# Whether HTTP auth or OAuth is enabled
ALLOW_EMPTY_HTTP_AUTH = get_bool_env('ALLOW_EMPTY_HTTP_AUTH', 'False')
OAUTH_ENABLED = get_bool_env('OAUTH_ENABLED', 'False')

# OAuth1 callback views
OAUTH_AUTHORIZE_VIEW = 'oauth_provider.views.authorize_client'
OAUTH_CALLBACK_VIEW = 'oauth_provider.views.callback_view'
OAUTH_SIGNATURE_METHODS = ['plaintext', 'hmac-sha1', 'rsa-sha1']

AUTH_USER_MODEL = "auth.User"
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {'min_length': 8}
    },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'}
]

# OAuth scopes
STATE = 1
PROFILE = 1 << 1
DEFINE = 1 << 2
STATEMENTS_READ_MINE = 1 << 3
STATEMENTS_READ = 1 << 4
STATEMENTS_WRITE = 1 << 5
ALL_READ = 1 << 6
ALL = 1 << 7

OAUTH_SCOPES = (
    (STATEMENTS_WRITE, 'statements/write'),
    (STATEMENTS_READ_MINE, 'statements/read/mine'),
    (STATEMENTS_READ, 'statements/read'),
    (STATE, 'state'),
    (DEFINE, 'define'),
    (PROFILE, 'profile'),
    (ALL_READ, 'all/read'),
    (ALL, 'all')
)

# AMPQ settings
AMPQ_USERNAME = os.environ.get('AMPQ_USERNAME', 'guest')
AMPQ_PASSWORD = os.environ.get('AMPQ_PASSWORD', 'guest')
AMPQ_HOST = os.environ.get('AMPQ_HOST', 'localhost')
AMPQ_PORT = int(os.environ.get('AMPQ_PORT', '5672'))
AMPQ_VHOST = os.environ.get('AMPQ_VHOST', '/')

CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_STORE_ERRORS_EVEN_IF_IGNORED = True
CELERY_IGNORE_RESULT = True

# Limit on number of statements the server will return
SERVER_STMT_LIMIT = int(os.environ.get('SERVER_STMT_LIMIT', '100'))

# Celery task timeouts
CELERYD_TASK_SOFT_TIME_LIMIT = 15

# ActivityID resolve timeout (seconds)
ACTIVITY_ID_RESOLVE_TIMEOUT = 0.2

# Caches for /more endpoint and attachments
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_statement_list',
        'TIMEOUT': 86400,
    },
    'attachment_cache': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'attachment_cache',
        'TIMEOUT': 86400,
    },
}

# Static files finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Secret key
SECRET_KEY = os.environ.get('SECRET_KEY', '_secret_')

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # Add template directories here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                "adl_lrs.context_processors.recaptcha_config"
            ],
        },
    },
]

# CORS and security settings
USE_ETAGS = False
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = (
    'HEAD', 'POST', 'GET', 'OPTIONS', 'DELETE', 'PUT'
)
CORS_ALLOW_HEADERS = (
    'Content-Type', 'Content-Length', 'Authorization',
    'If-Match', 'If-None-Match', 'X-Experience-API-Version', 'Accept-Language'
)
CORS_EXPOSE_HEADERS = (
    'ETag', 'Last-Modified', 'Cache-Control', 'Content-Type',
    'Content-Length', 'WWW-Authenticate', 'X-Experience-API-Version', 'Accept-Language'
)
CORS_URLS_REGEX = r"^/(xapi|xAPI)/.*$"

# Redis settings for Defender
DEFENDER_REDIS_URL = os.environ.get('DEFENDER_REDIS_URL', 'redis://localhost:6379/0')

# Middleware configuration
MIDDLEWARE = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'defender.middleware.FailedLoginMiddleware',
)

# Main URL configuration
ROOT_URLCONF = 'adl_lrs.urls'

# WSGI application
WSGI_APPLICATION = 'adl_lrs.wsgi.application'

# Admin registration
ADMIN_REGISTER_APPS = ['adl_lrs', 'lrs', 'oauth_provider']

# Installed apps
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adl_lrs',
    'captcha',
    'lrs',
    'oauth_provider',
    'django.contrib.admin',
    'jsonify',
    'corsheaders',
    'defender'
]

# Logging directories
REQUEST_HANDLER_LOG_DIR = os.path.join(PROJECT_ROOT, 'logs/django_request.log')
DEFAULT_LOG_DIR = os.path.join(PROJECT_ROOT, 'logs/lrs.log')
CELERY_TASKS_LOG_DIR = os.path.join(PROJECT_ROOT, 'logs/celery/celery_tasks.log')

CELERYD_HIJACK_ROOT_LOGGER = False

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': DEFAULT_LOG_DIR,
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': REQUEST_HANDLER_LOG_DIR,
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'celery_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': CELERY_TASKS_LOG_DIR,
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'lrs': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'WARNING',
            'propagate': True
        },
        'celery-task': {
            'handlers': ['celery_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
    }
}
