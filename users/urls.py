from django.urls import path
from .views import logoutUser, profiles, register, userAccount, userProfile, loginUser

urlpatterns = [

    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', register, name='register'),
    path('account/', userAccount, name='account'),

    path('', profiles, name='profiles'),
    path('profile/<str:pk>/', userProfile, name='user-profile')
]
