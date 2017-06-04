from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# TODO: Remove main_label from labels list
class List(models.Model):
    description = models.CharField(max_length=256, null=True, blank=True)
    main_label = models.ForeignKey(Label, related_name='lists')
    labels = models.ManyToManyField(Label, blank=True)
    # author = models.ForeignKey()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.main_label}'


class Task(models.Model):
    levels = (
        'low',
        'medium',
        'high',
        'critical'
    )
    PRIORITY_CHOICES = tuple(item for item in zip(range(1, len(levels)+1), levels))

    list = models.ForeignKey(List, null=True, blank=True, related_name='tasks')
    text = models.CharField(max_length=256)
    comment = models.TextField(null=True, blank=True)
    priority = models.IntegerField(default=1, choices=PRIORITY_CHOICES)
    resolved = models.BooleanField(default=False)
    # resolved_as = models.IntegerField(default=1, choices=RESOLVED_STATUS)
    resolved_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        resolved_symbol = '+' if self.resolved else '-'
        return f'{self.text} ({self.get_priority_display()}, {resolved_symbol})'
