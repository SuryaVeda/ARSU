from ARSU.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'aiims',
        'USER': 'postgres',
        'PASSWORD': 'SU@@1997',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
try:
    from ARSU.settings.local import *
except:
    pass
