from ARSU.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['178.32.245.193']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
DATABASES = {
            
}
try:
    from ARSU.settings.local import *
except:
    pass
