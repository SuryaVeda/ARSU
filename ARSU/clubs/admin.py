from django.contrib import admin
from .models import Clubs, Categories, Events
# Register your models here.
admin.site.register(Clubs)
admin.site.register(Categories)
admin.site.register(Events)
