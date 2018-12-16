"""Register filters."""
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from django_filters import rest_framework as filters

from account.models import User
from register import models


class TaskListFilter(filters.FilterSet):
    title = filters.CharFilter(
        lookup_expr='icontains', label=_('Title')
    )
    status = filters.NumberFilter()
    project_id = filters.ModelMultipleChoiceFilter(
        queryset=models.Task.objects.all()
    )
    author_id = filters.ModelMultipleChoiceFilter(
        queryset=User.objects.all()
    )
    executor_id = filters.ModelMultipleChoiceFilter(
        queryset=User.objects.all()
    )

    class Meta:
        model = models.Task
        fields = (
            'title',
            'status',
            'author_id',
            'executor_id',
            'project_id',
        )
