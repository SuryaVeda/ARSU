from ARSU.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['*']
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aiims',
        'USER': 'u_surya',
        'PASSWORD': 'SU@@1997',
        'HOST': 'localhost',
        'PORT': '5432',
    }        
}
try:
    from ARSU.settings.local import *
except:
    pass
