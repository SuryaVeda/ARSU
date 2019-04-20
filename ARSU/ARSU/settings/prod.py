from ARSU.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

try:
    from ARSU.settings.local import *
except:
    pass
