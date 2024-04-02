from django.urls import path, include
from rest_framework_nested import routers

from .views import ProjectViewSet, TaskViewSet

project_router = routers.DefaultRouter()
project_router.register('projects', ProjectViewSet, basename='projects')

tasks_router = routers.NestedSimpleRouter(project_router, 'projects', lookup='project')
tasks_router.register('tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(project_router.urls)),
    path('', include(tasks_router.urls)),
]
