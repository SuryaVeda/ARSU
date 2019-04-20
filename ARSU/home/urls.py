from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
path('', views.home, name='home'),
path('AcadForm', views.AcadForm, name = 'Acad'),
path('NAcadForm', views.NAcadForm, name = 'NAcad'),
path('HospitalNewsForm', views.HNForm, name = 'Hosp'),
path('CampusNewsForm', views.CNForm, name = 'Camp'),
path('search', views.search, name = 'search'),
]
