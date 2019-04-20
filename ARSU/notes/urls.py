from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
path('', views.notes, name = 'notes'),
path('subject_form', views.subject_form, name = 'subject'),
path('form', views.posts, name = 'posts'),
path('search', views.search, name = 'search'),

]
