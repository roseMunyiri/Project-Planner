from rest_framework import serializers
from .models import Project, Task

        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'description','start_date', 'due_date', 'status',  'priority',  'assignee','attachments']

    
class ProjectDetailSerializer(serializers.ModelSerializer):
    # project_duration = serializers.SerializerMethodField()
    # start_date = serializers.DateField(write_only=True)
    # due_date = serializers.DateField(write_only=True)
    tasks = TaskSerializer( many=True, read_only=True, source='task')

    class Meta:
        model = Project
        fields = ['id', 'name', 'tasks']

    
class ProjectSerializer(serializers.ModelSerializer):
    project_duration = serializers.SerializerMethodField()
    start_date = serializers.DateField(write_only=True)
    due_date = serializers.DateField(write_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'attachments', 'status', 'created_at', 'start_date', 'due_date', 'project_duration']

    def get_project_duration(self, obj):
        if obj.start_date and obj.due_date:
            project_duration = obj.due_date - obj.start_date
            return project_duration.days
        else:
            return None


        