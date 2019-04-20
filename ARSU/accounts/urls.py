from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
path('login', views.login, name = 'login' ),
path('signup/visitor', views.visitor, name='visitor' ),
path('signup/student', views.student, name = 'student'),
path('signup/CR', views.cr, name = 'cr'),
]
