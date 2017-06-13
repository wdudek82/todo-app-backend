from ..models import List, Task
from .serializers import ListSerializer, TaskSerializer
from rest_framework import generics, permissions


class ListListAPIView(generics.ListAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskListAPIView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
