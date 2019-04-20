from django.urls import path
from . import views
from .models import Clubs

app_name = 'clubs'

urlpatterns = [
path('', views.clubs, name = 'clubs'),
path('FineArts', views.FineArts, name = 'Fine Arts'),
path('cultural', views.cultural, name = 'Cultural Activites'),
path('literary', views.literary, name = 'Literary Activites'),
path('sports', views.sports, name = 'Sports'),
path('Magazine', views.magazine, name = 'Magazine'),
path('EventForm', views.posts, name = 'EventForm')
]
