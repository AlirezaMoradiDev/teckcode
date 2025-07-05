from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('error_not_access', views.error_not_access, name='not_access'),
    path('sign_up_instructor', views.register_instructor, name='signup'),
    path('profile/<str:username>', views.profile_instructor, name='profile')
]
