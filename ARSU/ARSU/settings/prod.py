from ARSU.settings.base import *

DEBUG = False
ALLOWED_HOSTS = ['*']


try:
    from ARSU.settings.local import *
except:
    pass
