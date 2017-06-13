from ..models import List, Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    priority = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'list', 'text', 'comment', 'priority', 'resolved', 'resolved_at',
                  'created_at', 'updated_at']

    def get_priority(self, instance):
        return instance.get_priority_display()

    def validate_text(self, attrs, source):
        print('attrs: ' + attrs)
        print('source: ' + source)
        return attrs


class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = List
        fields = ['id', 'title', 'description', 'tasks', 'is_active', 'created_at', 'updated_at']


# TODO: Add some validation (e.g.: validate_text(self.attrs, source)