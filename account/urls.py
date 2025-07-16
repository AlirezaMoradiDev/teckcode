from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('error_not_access', views.ErrorNotAccessPage.as_view(), name='not_access'),
    path('sign_up_instructor', views.register_instructor, name='signup'),
    path('list/<int:id>', views.SkillProfile.as_view(), name='list'),
    path('profile/<str:username>', views.ProfileInstructor.as_view(), name='profile')
]
