# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from account.models import User
from register import models


class BaseRegisterTestAPI(TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("\nStart test register app")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("End test register app")

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='TestUser', email='test@test.local', password='T1o3r9n5t0o')
        self.user.save()

        # Create task project
        self.project = models.TaskProject.objects.create(title='Task tracker')

        # Create task
        self.task = models.Task.objects.create(title='Create test for task',
                                               author=self.user,
                                               executor=self.user,
                                               project=self.project)


    def test_task_list(self):
        """
        Ensure we can list task.
        """
        url = reverse('task_list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_detail(self):
        """
        Ensure we can detail task.
        """
        url = reverse('task_retrieve', kwargs={'pk': self.task.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_update(self):
        """
        Ensure we can update task.
        """
        data = {
            'status': models.Task.IN_PROGRESS,
            'executor_id': self.user.id,
        }
        url = reverse('task_update', kwargs={'pk': self.task.id})
        response = self.client.patch(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_task_delete(self):
        """
        Ensure we can delete task.
        """
        url = reverse('task_delete', kwargs={'pk': self.task.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_task_create(self):
        """
        Ensure we can create task.
        """
        data = {
            'title': 'Create test for task',
            'author_id': self.user.id,
            'executor_id': self.user.id,
            'project_id': self.project.id
        }
        url = reverse('task_create')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_comment_create(self):
        """
        Ensure we can create comment.
        """
        data = {
            'text': 'I can do that.',
            'author_id': self.user.id,
            'task': self.task.id,
        }
        url = reverse('comment_create')
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
