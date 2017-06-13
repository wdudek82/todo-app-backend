from django.conf.urls import include, url


urlpatterns = [
    url(r'^todo/', include('apps.todo.api.urls', namespace='todo')),
]