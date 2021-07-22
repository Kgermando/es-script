import dj_database_url
from .settings import *


DEBUG = False
TEMPLATES_DEBUG = False

DATABASES['default'] = dj_database_url.config()


ALLOWED_HOSTS = ['crm-advans.herokuapp.com']