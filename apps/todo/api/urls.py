from django.conf.urls import url
from .views import ListListAPIView, TaskListAPIView


urlpatterns = [
    url(r'^tasks-list/list/$', ListListAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/$', ListListAPIView.as_view()),

    url(r'^task/list/$', TaskListAPIView.as_view()),
]
