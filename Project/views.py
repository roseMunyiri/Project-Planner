from rest_framework import status, viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import ProjectSerializer, ProjectDetailSerializer, TaskSerializer
from .models import Project
from .models import Task



class ProjectViewSet(ModelViewSet):
        
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related('task')

    def get_serializer_class(self):
        if self.kwargs:
            return ProjectDetailSerializer
        return ProjectSerializer
     
    
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save(project_id=self.kwargs.get('project_pk'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



