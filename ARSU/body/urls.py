from django.urls import path
from . import views


app_name = 'body'
urlpatterns = [
path('', views.body , name = 'body'),
path('add', views.addStudent, name = 'add'),
path('details', views.details, name = 'details'),
path('edit/<int:id>', views.editForm , name = 'change'),
]
