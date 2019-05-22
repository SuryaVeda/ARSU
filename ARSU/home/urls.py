from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
path('', views.home, name='home'),
path('ScheduleForm', views.schedule, name = 'schedule'),
path('AttendanceForm', views.attendance, name = 'attendance'),
path('ResultsForm', views.results, name = 'results'),
path('NAcadForm', views.NAcadForm, name = 'NAcad'),
path('CampusNewsForm', views.CNForm, name = 'Camp'),
path('search', views.search, name = 'search'),
path('del/<int:id>', views.ScheDel, name = 'schedule_delete'),
path('delRe/<int:id>', views.ReDel, name = 'results_delete'),
path('delAtt/<int:id>', views.AttDel, name = 'attendance_delete'),
path('delCamp/<int:id>', views.CampDel, name = 'camp_delete'),
path('delNaca/<int:id>', views.NacaDel, name = 'naca_delete'),


]
