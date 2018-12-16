# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.mixins import ProjectBaseMixin


class Task(ProjectBaseMixin):
    """Task model."""
    TODO = 0
    IN_PROGRESS = 1
    DONE = 2

    STATUS_CHOICES = (
        (TODO, _('To Do')),
        (IN_PROGRESS, _('In Progress')),
        (DONE, _('Done'))
    )

    title = models.CharField(
        _('Title'), max_length=150)

    status = models.PositiveSmallIntegerField(
        _('Status'), choices=STATUS_CHOICES, default=TODO)

    author =  models.ForeignKey(
        'account.User', verbose_name=_('Author'),
        related_name='created_tasks', on_delete=models.CASCADE)

    executor = models.ForeignKey(
        'account.User', verbose_name=_('Executor'),
        related_name='executable_tasks', null=True,
        blank=True, default=None, on_delete=models.CASCADE)

    project = models.ForeignKey(
        'register.TaskProject', verbose_name=_('Project'),
        blank=True, null=True, default=None, on_delete=models.CASCADE)


    class Meta:
        verbose_name = _('Task')
        verbose_name_plural = _('Tasks')
        ordering = ('modified', 'created', 'id')

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


class TaskDescription(ProjectBaseMixin):
    """Description of tasks model."""
    task = models.ForeignKey(
        Task, verbose_name=_('Task'), related_name='descriptions', on_delete=models.CASCADE)

    text = models.TextField(
        _('Text'))

    class Meta:
        verbose_name = _('Description')
        verbose_name_plural = _('Descriptions')


class TaskProject(ProjectBaseMixin):
    """Project of tasks model."""
    title = models.CharField(
        _('Title'), max_length=150)

    class Meta:
        verbose_name = _('Task project')
        verbose_name_plural = _('Task projects')


class Comment(ProjectBaseMixin):
    author = models.ForeignKey(
        'account.User', verbose_name=_('Author'), related_name='comments', on_delete=models.CASCADE)

    task = models.ForeignKey(
        'register.Task', verbose_name=_('Task'), related_name='comments', on_delete=models.CASCADE)

    text = models.TextField(
        _('Text'))

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')
