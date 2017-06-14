from django.conf.urls import url
from .views import UserViewSet


urlpatterns = [
    url(r'^users/$', UserViewSet.as_view(), name='users'),
]