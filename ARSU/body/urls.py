from django.urls import path
from . import views


app_name = 'body'
urlpatterns = [
path('', views.body , name = 'body'),
path('details', views.details , name = 'details')
]
