from rest_framework import serializers
from .models import Task
from Project.serializers import ProjectSerializer
from Account.serializers import UserSerializer


class TaskSerializer(serializers.ModelSerializer):
    related_project = ProjectSerializer(read_only=True)
    assignee = UserSerializer (many=True)
    class Meta:
        model = Task
        fields = '__all__'
        extra_kwargs = {
            'assignee': {'required': False}
        }