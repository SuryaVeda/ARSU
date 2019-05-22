from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
path('signin', views.signin, name = 'login' ),
path('signup/visitor', views.visitor, name='visitor' ),
path('signup/student', views.student, name = 'student'),
path('signup/CR', views.cr, name = 'cr'),
path('profile', views.profile, name = 'profile'),
path('profileForm/<int:id>', views.profileForm, name = 'profileForm'),
path('timetable', views.table, name = 'table'),
path('activities', views.activities, name = 'activities'),
path('remainders', views.remainders, name = 'remainders'),
path('Rdel/<int:obj_id>', views.Rdel, name = 'Rdel'),
path('Tdel/<int:obj_id>', views.Tdel, name = 'Tdel'),
path('Adel/<int:obj_id>', views.Adel, name = 'Adel'),

]
