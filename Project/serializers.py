from rest_framework import serializers
from .models import AbstractBaseModel, Project


class AbstractBaseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbstractBaseModel
        fields = '__all__' 

