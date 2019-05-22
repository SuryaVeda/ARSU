from django.contrib import admin
from home.models import  NonAcademic, CampusNews,  batches, Carousel, Schedule,Attendance, Results
# Register your models here.
admin.site.register(batches)
admin.site.register(NonAcademic)
admin.site.register(CampusNews)
admin.site.register(Carousel)
admin.site.register(Schedule)
admin.site.register(Attendance)
admin.site.register(Results)
