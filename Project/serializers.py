from rest_framework import serializers
from .models import AbstractBaseModel, Project
from Account.serializers import UserSerializer


class AbstractBaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractBaseModel
        fields = '__all__' 

class ProjectSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True, read_only=True)
    assignee = UserSerializer(many=True, read_only=True )
    
    class Meta:
        model = Project
        fields = '__all__'
    