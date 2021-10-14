from django.urls import path
from .views import (editAccount, logoutUser, profiles, register, userAccount,
                    userProfile, loginUser, createSkill, updateSkill, deleteSkill,
                    inbox, viewMessage, createMessage)

urlpatterns = [

    path('login/', loginUser, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', register, name='register'),
    path('account/', userAccount, name='account'),

    path('', profiles, name='profiles'),
    path('profile/<str:pk>/', userProfile, name='user-profile'),

    path('edit-account/', editAccount, name='edit-account'),

    path('create-skill/', createSkill, name='createskill'),
    path('update-skill/<str:pk>/', updateSkill, name='updateskill'),
    path('delete-skill/<str:pk>/', deleteSkill, name='deleteskill'),

    path('inbox/', inbox, name='inbox'),
    path('message/<str:pk>/', viewMessage, name='message'),
    path('compose-message/<str:pk>/', createMessage, name='compose-message'),
]
