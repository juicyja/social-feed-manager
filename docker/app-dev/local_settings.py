import os

DEBUG = os.getenv('SFM_DEBUG', 'True') == 'True'

ADMINS = (
    (os.getenv('SFM_ADMIN_NAME', 'sfmadmin'), os.getenv('SFM_ADMIN_EMAIL', 'nowhere@example.com')),
)

MANAGERS = ADMINS

# This value should be something like [sfm-test] (with a trailing space)
EMAIL_SUBJECT_PREFIX = ' '

# Set SERVER_EMIL to root@myserver, e.g. 'root@gwsfm-test.wrlc.org'
SERVER_EMAIL = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sfm',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'db',
        'PORT': '5432',
    }
}

ALLOWED_HOSTS = ['YOUR.PUBLIC.DOMAIN.NAME']

# See https://docs.djangoproject.com/en/1.4/topics/cache/
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'your-unique-sfm-instance-name',
    }
}

TEMPLATE_DIRS = (
)

DATA_DIR = '/var/sfm'

# If not specified, the supervisor configuration files
# will use the owner of the sfm app process.  The owner must
# be able to write to /var/log/sfm
#SUPERVISOR_PROCESS_USER = ''

# Path to the supervisor Unix socket file (with no unix:// prefix)
# e.g. '/var/run/supervisor.sock'.  Note that this must match the Unix
# socket file specified in /etc/supervisor/supervisord.conf
SUPERVISOR_UNIX_SOCKET_FILE = '/var/run//supervisor.sock'

TWITTER_DEFAULT_USERNAME = os.environ['SFM_TWITTER_DEFAULT_USERNAME']
TWITTER_CONSUMER_KEY = os.environ['SFM_TWITTER_CONSUMER_KEY']
TWITTER_CONSUMER_SECRET = os.environ['SFM_TWITTER_CONSUMER_SECRET']

BRANDING = {
    # Required:
    'institution': '',
    'URL': '',
    # Optional:
    #   address may contain any number of elements
    'address': ['', '', ''],
    'email': '',
    #   logofile should be placed in static/img
    'logofile': '',
}

#Use django-finalware to create the superadmin account.
#Redefining INSTALLED_APPS could be replaced with this hack: http://blog.christopherlawlor.com/2010/06/django-how-to-add-debugging-apps-to-your-local-settings/
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'social_auth',
    'south',
    'ui',
    'finalware'
)
# This field is the superuser object ID. Pick something other than `1` for security reason.
SITE_SUPERUSER_ID = '5'

# This field is stored in `User.USERNAME_FIELD`. This is usually a `username` or  an `email`.
SITE_SUPERUSER_USERNAME = os.getenv('SFM_ADMIN_NAME', 'sfmadmin')

# This field is stored in the `email` field, provided, that `User.USERNAME_FIELD` is not an `email`.
# If `User.USERNAME_FIELD` is already an email address, set `SITE_SUPERUSER_EMAIL = SITE_SUPERUSER_USERNAME`
SITE_SUPERUSER_EMAIL = os.getenv('SFM_ADMIN_EMAIL', 'nowhere@example.com')

# A hashed version of `SITE_SUPERUSER_PASSWORD` will be store in superuser's `password` field.
SITE_SUPERUSER_PASSWORD = os.getenv('SFM_ADMIN_PASSWORD', 'password')

SUPERVISOR_ROOT = "/var/sfm/supervisor.d"