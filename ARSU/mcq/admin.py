from django.contrib import admin
from .models import Topic, Mcq, FlashCard, Fact
# Register your models here.
admin.site.register(Topic)
admin.site.register(Mcq)
admin.site.register(FlashCard)
admin.site.register(Fact)
