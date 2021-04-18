
from django.urls import path

from accounts.views import login_view, register_view, logout_view, profile, profile_edit


urlpatterns = [
    path('', login_view, name='login'),
    path('register/', register_view, name='register'), 
    path('logout/', logout_view, name='logout'),

    path('profile/', profile, name='profile'),
    path('profile_edit/<int:pk>/user', profile, name='profile_edit'),
]
