from django.urls import path
from .views import projects, project, createProject, updateProject, deleteProject

urlpatterns = [
    path('', projects, name='projects'),
    path('project/<str:pk>/', project, name='project'),

    path('create-project/', createProject, name='createproject'),
    path('update-project/<str:pk>/', updateProject, name='updateproject'),
    path('delete-project/<str:pk>/', deleteProject, name='deleteproject'),

]
