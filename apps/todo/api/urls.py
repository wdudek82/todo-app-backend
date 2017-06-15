from django.conf.urls import url
from .views import ListListAPIView, TaskListAPIView
from .views import TasksList, TaskListDetail


urlpatterns = [
    # Generic CBV
    url(r'^tasks-list/list/$', ListListAPIView.as_view()),
    url(r'^task/list/$', TaskListAPIView.as_view()),

    # CBV
    url(r'^task-list/(?P<pk>\d+)/$', TaskListDetail.as_view()),
    url(r'^task-list/$', TasksList.as_view()),
]
