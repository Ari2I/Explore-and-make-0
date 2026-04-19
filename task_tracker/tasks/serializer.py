from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Project, Task, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email'
        ]


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'owner',
            'participants'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        project = Project.objects.create(owner=user, **validated_data)
        project.participants.add(user)
        return project


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'project',
            'author',
            'performer',
            'status',
            'priority',
            'deadline'
        ]

    def create(self, validated_data):
        user = self.context['request'].user
        return Task.objects.create(author=user, **validated_data)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = [
            'id',
            'task',
            'author',
            'text',
            'created_at'
        ]
    def create(self, validated_data):
        user = self.context['request'].user
        return Comment.objects.create(author=user, **validated_data)