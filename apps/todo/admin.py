from django.contrib import admin
from django.utils.html import format_html_join, format_html, mark_safe
from .models import Label, List, Task


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated_at']
    list_display_links = ['name']


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = ['id', 'main_label', 'get_labels', 'description', 'get_tasks', 'is_active',
                    'created_at', 'updated_at']
    list_display_links = ['main_label']
    filter_horizontal = ['labels']
    inlines = [TaskInline]
    list_filter = ['main_label', 'created_at', 'updated_at']
    search_fields = ['labels_name', 'tasks__text']

    def get_labels(self, instance):
        labels = [str(label) for label in instance.labels.all()]
        return mark_safe('<br>'.join(labels)) if labels else '-'
    get_labels.short_description = 'labels'

    def get_tasks(self, instance):
        tasks = [f'<li>{str(task)}</li>' for task in instance.tasks.all()]
        formatted = format_html('<ol>{}</ol>', mark_safe(''.join(tasks)))
        return formatted if tasks else '-'
    get_tasks.short_description = 'tasks'


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'list', 'text', 'resolved', 'resolved_at', 'created_at', 'updated_at']
    list_filter = ['list', 'created_at', 'updated_at']
    search_fields = ['text']
