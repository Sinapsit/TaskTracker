from __future__ import unicode_literals

from rest_framework import serializers

from account.models import User
from register import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email'
        ]

class TaskDescriptionsSerializer(serializers.ModelSerializer):
    """Task descriptions serializer."""
    task_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Task.objects.all(),
        source='task',
        write_only=True
    )

    class Meta:
        model = models.TaskDescription
        fields = [
            'id',
            'task_id',
            'text'
        ]




class CommentSerializers(serializers.ModelSerializer):
    """Comment serializers."""
    author = UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='author', write_only=True)

    class Meta:
        model = models.Comment
        fields = [
            'id',
            'author',
            'author_id',
            'task',
            'text'
        ]

class CommentShortSerializers(serializers.ModelSerializer):
    """Comment serializers."""
    author = UserSerializer(read_only=True)
    class Meta:
        model = models.Comment
        fields = [
            'id',
            'author',
            'text'
        ]


class ProjectSerializers(serializers.ModelSerializer):
    """Project serializers."""
    class Meta:
        model = models.TaskProject
        fields = [
            'id',
            'title'
        ]


class TaskSerializers(serializers.ModelSerializer):
    """Task serializers."""
    descriptions = TaskDescriptionsSerializer(many=True, read_only=True)
    comments = CommentShortSerializers(many=True, read_only=True)
    author = UserSerializer(read_only=True)
    executor = UserSerializer(read_only=True)
    project = ProjectSerializers(read_only=True)
    status_display = serializers.CharField(read_only=True, source='get_status_display')

    class Meta:
        model = models.Task
        fields = [
            'id',
            'title',
            'author',
            'status',
            'status_display',
            'executor',
            'project',
            'descriptions',
            'comments'
        ]


class TaskUpdateSerializers(serializers.ModelSerializer):
    """Task serializers."""
    descriptions = TaskDescriptionsSerializer(many=True, read_only=True)
    comments = CommentShortSerializers(many=True, read_only=True)
    author = UserSerializer(read_only=True)
    executor_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), source='executor', write_only=True)
    executor = UserSerializer(read_only=True)
    project = ProjectSerializers(read_only=True)
    class Meta:
        model = models.Task
        read_only_fields = [
            'title'
        ]
        fields = [
            'id',
            'title',
            'status',
            'author',
            'executor_id',
            'executor',
            'project',
            'descriptions',
            'comments'
        ]


class TaskCreateSerializers(serializers.ModelSerializer):
    """Task create serializers."""
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='author', write_only=True)

    author = UserSerializer(
        read_only=True)

    executor_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='executor', write_only=True)

    executor = UserSerializer(
        read_only=True)

    project_id = serializers.PrimaryKeyRelatedField(
        queryset=models.TaskProject.objects.all(), source='project', write_only=True)

    project = ProjectSerializers(
        read_only=True)

    class Meta:
        model = models.Task

        fields = [
            'id',
            'title',
            'status',
            'author_id',
            'author',
            'executor_id',
            'executor',
            'project_id',
            'project',
        ]