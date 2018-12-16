from __future__ import unicode_literals

from django.conf.urls import url

from register import views

urlpatterns = [
    url(r'task/$', views.TaskListView.as_view(), name='task_list' ),
    url(r'task/create/$', views.TaskCreateView.as_view(), name='task_create' ),
    url(r'task/(?P<pk>\d+)/$', views.TaskRetrieveView.as_view(), name='task_retrieve' ),
    url(r'task/(?P<pk>\d+)/update/$', views.TaskUpdateView.as_view(), name='task_update' ),
    url(r'task/(?P<pk>\d+)/delete/$', views.TaskDeleteView.as_view(), name='task_delete' ),
    url(r'comment/create/$', views.CommentCreateView.as_view(), name='comment_create'),
    url(r'project/create/$', views.ProjectCreateView.as_view(), name='project_create'),
]