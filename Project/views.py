from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import ProjectSerializer, ProjectDetailSerializer, TaskSerializer
from api.permissions import isAdminorReadOnly
from .models import Project
from .models import Task



class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [isAdminorReadOnly] 
        
    def get_queryset(self):
        user = self.request.user
        queryset = Project.objects.filter(project_creator=user)
        return queryset.prefetch_related('task')

    def get_serializer_class(self):
        if self.kwargs:
            return ProjectDetailSerializer
        return ProjectSerializer
    
    def perform_create(self, serializer):
        serializer.save(project_creator=self.request.user)
         
class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [isAdminorReadOnly]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        project_id = self.kwargs.get('project_pk')
        queryset = Task.objects.filter(project_id=project_id) | Task.objects.filter(assignee=user)
        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save( project_id = self.kwargs.get('project_pk'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



