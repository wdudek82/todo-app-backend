from django.conf.urls import url
from .views import ListsList, ListDetail, TaskList, TaskDetail


urlpatterns = [
    # Generic CBV
    # from .views import ListListAPIView, TaskListAPIView
    # url(r'^tasks-list/list/$', ListListAPIView.as_view()),
    # url(r'^task/list/$', TaskListAPIView.as_view()),

    # CBV
    # Lists
    url(r'^task-list/(?P<pk>\d+)/$', ListDetail.as_view()),
    url(r'^task-list/$', ListsList.as_view()),

    # Tasks
    url(r'^task/$', TaskList.as_view()),
    url(r'^task/(?P<pk>\d+)/$', TaskDetail.as_view()),
]
