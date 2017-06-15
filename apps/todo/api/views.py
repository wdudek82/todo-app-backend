from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ListSerializer, TaskSerializer
from ..models import List, Task


class ListsList(APIView):
    """
    List all task-lists, or create new

    """
    def get(self, request, format=None):
        task_lists = List.objects.all()
        serializer = ListSerializer(task_lists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListDetail(APIView):
    """
    Retrieve, update or delete a task list instance
    """
    def get(self, request, pk, format=None):
        task_list = get_object_or_404(List, pk=pk)
        serializer = ListSerializer(task_list)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task_list = get_object_or_404(List, pk=pk)
        serializer = ListSerializer(task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task_list = get_object_or_404(List, pk=pk)
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskList(APIView):
    """
    List all tasks or create new
    """
    def get(self, request, format=None):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    """
    Retrieve, update or delete a task instance
    """
    def get(self, request, pk, format=None):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###############
### Generic CBV
###############
# from rest_framework import generics, permissions
# class ListListAPIView(generics.ListAPIView):
#     queryset = List.objects.all()
#     serializer_class = ListSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class TaskListAPIView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticated]
