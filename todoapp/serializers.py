from .models import Project, Todo
from rest_framework import serializers


class ProjectModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'repo', 'users']


class TodoModelSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.StringRelatedField(many=True)
    class Meta:
        model = Todo
        fields = ['project', 'text', 'creator', 'created', 'updated', 'is_active']
