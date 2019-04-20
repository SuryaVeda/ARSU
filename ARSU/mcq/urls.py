from django.urls import path
from . import views

app_name = 'mcq'

urlpatterns = [
path('', views.subs, name = 'sticky'),
path('Anatomy', views.Anatomy, name = 'Anatomy'),
path('Physiology', views.Physiology, name = 'Physiology'),
path('Biochemistry', views.Biochemistry, name = 'Biochemistry'),
path('Pathology', views.Pathology, name = 'Pathology'),
path('Pharmacology', views.Pharmacology, name = 'Pharmacology'),
path('Microbiology', views.Microbiology, name = 'Microbiology'),
path('Forensics', views.Forensic, name = 'Forensics'),
path("optha", views.optha, name = "optha" ),
path('ENT', views.ENT, name = 'ENT'),
path('Orthopaedics', views.Orthopaedics, name = 'Orthopaedics'),
path('CFM', views.CFM, name = 'CFM'),
path('Medicine', views.Medicine, name = 'Medicine'),
path('Surgery', views.Surgery, name = 'Surgery'),
path('Pediatrics', views.Pediatrics, name = 'Pediatrics'),
path('OBG', views.OBG, name = 'OBG'),
path('AddMcq', views.addMcq, name = 'forms'),
path('AddTopic', views.addTopic, name = 'addTopic'),
path('search', views.search, name = 'search'),

]
