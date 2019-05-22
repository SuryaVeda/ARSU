from django.urls import path
from . import views

app_name = 'mcq'

urlpatterns = [
path('', views.subs, name = 'sticky'),
path('AddMcq/<int:id>/<int:pk>', views.mcq, name = 'forms'),
path('AddFacts/<int:id>/<int:pk>', views.facts, name = 'fact'),
path('AddCards/<int:id>/<int:pk>', views.cards, name = 'card'),
path('AddTopic/<int:id>', views.topic, name = 'addTopic'),
path('search', views.search, name = 'search'),
path('<int:id>', views.sub, name = 'hola'),
]
