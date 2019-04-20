from django.contrib import admin
from home.models import Academic, NonAcademic, HospitalNews, CampusNews,  batches, Carousel
# Register your models here.
admin.site.register(Academic)
admin.site.register(batches)
admin.site.register(NonAcademic)
admin.site.register(HospitalNews)
admin.site.register(CampusNews)
admin.site.register(Carousel)
