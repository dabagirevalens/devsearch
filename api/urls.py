from django.urls import path

from .views import getProject, getProjects, getRoutes


urlpatterns = [ 
    path('', getRoutes),
    path('projects/', getProjects),
    path('projects/<str:pk>', getProject),
]