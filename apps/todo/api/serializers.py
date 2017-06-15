from rest_framework import serializers

from ..models import List, Task


# TODO: Add some validation (e.g.: validate_text(self.attrs, source)
class TaskSerializer(serializers.ModelSerializer):
    priority = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ['id', 'list', 'text', 'comment', 'priority', 'resolved', 'resolved_at',
                  'created_at', 'updated_at']

    def get_priority(self, instance):
        return instance.get_priority_display()

    def validate_text(self, text):
        print('text: ' + text)
        return text

    def validate_comment(self, comment):
        print('commend: ' + comment)
        return comment


class ListSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = List
        fields = ['id', 'title', 'description', 'tasks', 'is_active', 'created_at', 'updated_at']
