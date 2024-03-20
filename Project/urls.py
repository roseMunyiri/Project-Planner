from django.urls import path
from .views import ProjectListCreateView, ProjectRetrieveUpdateDestroyView

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-retrieve-update-destroy'),
]
