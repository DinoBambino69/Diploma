from django.urls import path
from src.users.views import (RegisterUser, UsersProfileCreateView, user_login,
                             user_logout, UsersProfileDetailView, UsersProfileUpdateView, StartPrediction)

urlpatterns = [
    path('', UsersProfileDetailView.as_view(), name='main'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/update', UsersProfileUpdateView.as_view(), name='update'),
    path('profile/create', UsersProfileCreateView.as_view(), name='profile'),
    path('profile/ai', StartPrediction, name='ai'),
]
