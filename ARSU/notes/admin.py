from django.contrib import admin
from .models import subject, Ebook, Paper, Lecture
# Register your models here.
admin.site.register(subject)
admin.site.register(Ebook)
admin.site.register(Paper)
admin.site.register(Lecture)
