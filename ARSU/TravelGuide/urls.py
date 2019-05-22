from django.urls import path
from . import views

app_name = 'TravelGuide'

urlpatterns = [
path('', views.travel, name = 'travel'),
path('addTrip', views.addTrip, name = 'addTrip'),
path('addImages/<int:id>', views.addImages, name = 'addImages'),
path('editTrip/<int:id>', views.editTrip, name = 'editTrip'),

]
