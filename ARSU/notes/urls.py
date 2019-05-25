from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
path('', views.subs, name = 'subj'),
path('<int:id>', views.subs, name = 'notes'),
path('subject_form', views.subject_form, name = 'subject'),
path('Eform/<int:id>', views.Eposts, name = 'Epost'),
path('Pform/<int:id>', views.Pposts, name = 'Ppost'),
path('Lform/<int:id>', views.Lposts, name = 'Lpost'),
path('search', views.search, name = 'search'),

]
