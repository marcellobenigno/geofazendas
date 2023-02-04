import os
from pathlib import Path

from decouple import config, Csv
from dj_database_url import parse as db_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', default='123')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())
CSRF_TRUSTED_ORIGINS = [
    'https://www.geofazendas.com.br', 'https://geofazendas.com.br', 'http://local.geofazendas.com.br:8000',
    'http://127.0.0.1:8000', 'http://localhost:8000'
]

# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # GeoDjango
    'django.contrib.gis',
    # Third apps
    'rolepermissions',
    'localflavor',
    'django_extensions',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework.authtoken',
    'django_filters',
    'easy_select2',
    'ckeditor',
    'corsheaders',
    'bootstrap5',
    'taggit',
    'widget_tweaks',
    'martor',
    # Geofazendas Apps:
    'geofazendas.base.apps.CoreConfig',
    'geofazendas.artigos.apps.ArtigosConfig',
    'geofazendas.mapas.apps.MapasConfig',
    'geofazendas.seguranca.apps.SegurancaConfig',
    'geofazendas.sindicatos.apps.SindicatosConfig',
    'geofazendas.anuncios.apps.AnunciosConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'geofazendas.seguranca.middleware.LastAccessMiddleware',
]

ROOT_URLCONF = 'geofazendas.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'geofazendas.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': config(
        'DATABASE_URL', cast=db_url, default='postgresql://geofazendas:geofazendas@127.0.0.1/geofazendas'
    ),
}
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_THOUSAND_SEPARATOR = True

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# AUTH
AUTH_USER_MODEL = 'seguranca.Usuario'
ROLEPERMISSIONS_MODULE = 'geofazendas.roles'
LOGIN_URL = 'seguranca:login'
LOGIN_REDIRECT_URL = 'seguranca:inicio'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DATE_INPUT_FORMATS': ["%d/%m/%Y"],
    'DATE_FORMAT': '%d/%m/%Y',
    'DATETIME_FORMAT': '%d/%m/%Y %H:%M',
}

# MOBIZON SMS
SMS_API_TOKEN = 'bre464ced034c5c76461f2ad0a7c87456b37ee1067d1acb0a3f1d5d3b5d4ab798a29c9'
SMS_API_EMAIL = 'contato@multisig.com.br'
# django-admin-interface
X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

CORS_ALLOW_ALL_ORIGINS = True

EMAIL_HOST = 'email-smtp.us-east-1.amazonaws.com'
EMAIL_HOST_USER = 'AKIAYN6VKB7LW5XBYFUJ'
EMAIL_HOST_PASSWORD = 'BOVOVIvZA74xDB1L2KcuBr/LSHZsxWO5lJznVhmINTe5'
DEFAULT_FROM_EMAIL = 'desenvolvimento@multisig.com.br'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = config(
    'EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend'
)
SERVER_EMAIL = EMAIL_HOST_USER

ADMINS = (
    ('Marcello', 'benigno.marcello@gmail.com'),
    ('Gileno', 'contato@gilenofilho.com.br'),
)

# bootstrap
BOOTSTRAP5 = {
    'set_placeholder': False,
    'success_css_class': '',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': config('DJANGO_ERROR_LOG', default=os.path.join(BASE_DIR, 'django-error.log')),
            'formatter': 'verbose',
        },
        'file_debug': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django-debug.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', 'console', 'file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'sigitr.debug': {
            'handlers': ['file_debug'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

# GEOSERVER
GEOSERVER_URL = config('GEOSERVER_URL', default='http://127.0.0.1:8080/geoserver/itrfacil/wms')

# Martor
MARTOR_THEME = 'bootstrap'

# Global martor settings
# Input: string boolean, `true/false`
MARTOR_ENABLE_CONFIGS = {
    'emoji': 'true',        # to enable/disable emoji icons.
    'imgur': 'false',        # to enable/disable imgur/custom uploader.
    'mention': 'false',     # to enable/disable mention
    'jquery': 'true',       # to include/revoke jquery (require for admin default django)
    'living': 'false',      # to enable/disable live updates in preview
    'spellcheck': 'false',  # to enable/disable spellcheck in form textareas
    'hljs': 'true',         # to enable/disable hljs highlighting in preview
}

# To show the toolbar buttons
MARTOR_TOOLBAR_BUTTONS = [
    'bold', 'italic', 'horizontal', 'heading', 'pre-code',
    'blockquote', 'unordered-list', 'ordered-list',
    'link', 'image-link', 'image-upload', 'emoji',
    'direct-mention', 'toggle-maximize', 'help'
]

# To setup the martor editor with title label or not (default is False)
MARTOR_ENABLE_LABEL = False

# Imgur API Keys
MARTOR_IMGUR_CLIENT_ID = 'your-client-id'
MARTOR_IMGUR_API_KEY   = 'your-api-key'

# Markdownify
MARTOR_MARKDOWNIFY_FUNCTION = 'martor.utils.markdownify' # default
MARTOR_MARKDOWNIFY_URL = '/martor/markdownify/' # default

# Markdown extensions (default)
MARTOR_MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.nl2br',
    'markdown.extensions.smarty',
    'markdown.extensions.fenced_code',

    # Custom markdown extensions.
    'martor.extensions.urlize',
    'martor.extensions.del_ins',      # ~~strikethrough~~ and ++underscores++
    'martor.extensions.mention',      # to parse markdown mention
    'martor.extensions.emoji',        # to parse markdown emoji
    'martor.extensions.mdx_video',    # to parse embed/iframe video
    'martor.extensions.escape_html',  # to handle the XSS vulnerabilities
]

# Markdown Extensions Configs
MARTOR_MARKDOWN_EXTENSION_CONFIGS = {}

# Markdown urls
MARTOR_UPLOAD_URL = '/martor/uploader/' # default
MARTOR_SEARCH_USERS_URL = '/martor/search-user/' # default

# Markdown Extensions
# MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://www.webfx.com/tools/emoji-cheat-sheet/graphics/emojis/'     # from webfx
MARTOR_MARKDOWN_BASE_EMOJI_URL = 'https://github.githubassets.com/images/icons/emoji/'                  # default from github
MARTOR_MARKDOWN_BASE_MENTION_URL = 'https://www.geofazendas.com.br/'

# If you need to use your own themed "bootstrap" or "semantic ui" dependency
# replace the values with the file in your static files dir
MARTOR_ALTERNATIVE_JS_FILE_THEME = "semantic-themed/semantic.min.js"   # default None
MARTOR_ALTERNATIVE_CSS_FILE_THEME = "semantic-themed/semantic.min.css" # default None
MARTOR_ALTERNATIVE_JQUERY_JS_FILE = "jquery/dist/jquery.min.js"        # default None

# URL schemes that are allowed within links
ALLOWED_URL_SCHEMES = [
    "file", "ftp", "ftps", "http", "https", "irc", "mailto",
    "sftp", "ssh", "tel", "telnet", "tftp", "vnc", "xmpp",
]

# https://gist.github.com/mrmrs/7650266
ALLOWED_HTML_TAGS = [
    "a", "abbr", "b", "blockquote", "br", "cite", "code", "command",
    "dd", "del", "dl", "dt", "em", "fieldset", "h1", "h2", "h3", "h4", "h5", "h6",
    "hr", "i", "iframe", "img", "input", "ins", "kbd", "label", "legend",
    "li", "ol", "optgroup", "option", "p", "pre", "small", "span", "strong",
    "sub", "sup", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "u", "ul"
]

# https://github.com/decal/werdlists/blob/master/html-words/html-attributes-list.txt
ALLOWED_HTML_ATTRIBUTES = [
    "alt", "class", "color", "colspan", "datetime",  # "data",
    "height", "href", "id", "name", "reversed", "rowspan",
    "scope", "src", "style", "title", "type", "width"
]
