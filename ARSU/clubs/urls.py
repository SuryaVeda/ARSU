from django.urls import path
from . import views
from .models import Clubs

app_name = 'clubs'

urlpatterns = [
path('', views.clubs, name = 'clubs'),
path('EventForm/<int:id>', views.posts, name = 'EventForm'),
path('clubForm', views.addClub, name = 'addClubs'),
path('catForm/<int:id>', views.addCategories, name = 'cat'),
path('<int:id>', views.newClub, name = 'new'),
path('del/<int:id>', views.event_delete, name = 'delete'),

]
