"""Register filters."""
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django_filters import rest_framework as filters

from register import models


class TaskListFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains', label=_('Title'))

    class Meta:
        model = models.Task
        fields = (
            'title',
            'author_id',
            'executor_id',
            'project_id',
        )
