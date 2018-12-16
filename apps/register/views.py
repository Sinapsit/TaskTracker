# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from register import models
from register import serializers, filters


class TaskListView(generics.ListAPIView):
    """Task list view."""
    serializer_class = serializers.TaskSerializers
    pagination_class = None
    queryset = models.Task.objects.all()
    filter_class = filters.TaskListFilter
    filter_backends = (DjangoFilterBackend,)


class TaskRetrieveView(generics.RetrieveAPIView):
    """Task retrieve view."""
    serializer_class = serializers.TaskSerializers
    pagination_class = None
    queryset = models.Task.objects.all()


class TaskUpdateView(generics.UpdateAPIView):
    """Task update view.
    ### "status" field gets integer values:
        TO DO = 0
        IN PROGRESS = 1
        DONE = 2"""
    serializer_class = serializers.TaskUpdateSerializers
    pagination_class = None
    queryset = models.Task.objects.all()


class TaskDeleteView(generics.DestroyAPIView):
    """Task delete view."""
    serializer_class = serializers.TaskSerializers
    pagination_class = None
    queryset = models.Task.objects.all()


class TaskCreateView(generics.CreateAPIView):
    """Task create view.
    ### "status" field gets integer values:
        TO DO = 0
        IN PROGRESS = 1
        DONE = 2"""
    serializer_class = serializers.TaskCreateSerializers
    pagination_class = None
    queryset = models.Task.objects.all()


class CommentCreateView(generics.CreateAPIView):
    """Comment create view."""
    serializer_class = serializers.CommentSerializers
    pagination_class = None
    queryset = models.Comment.objects.all()


class ProjectCreateView(generics.CreateAPIView):
    """Project create view."""
    serializer_class = serializers.ProjectSerializers
    pagination_class = None
    queryset = models.TaskProject.objects.all()

class DescriptionCreateView(generics.CreateAPIView):
    """Description create view."""
    serializer_class = serializers.TaskDescriptionsSerializer
    pagination_class = None
    queryset = models.TaskDescription.objects.all()