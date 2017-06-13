from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver




class List(models.Model):
    title = models.CharField(max_length=256, blank=True)
    description = models.TextField(null=True, blank=True)
    # author = models.ForeignKey()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.title}'

    @staticmethod
    def get_list_title():
        now = str(timezone.now())[:16]
        return f'List {now}'


@receiver(pre_save, sender=List)
def pre_save_list(sender, instance, **kwargs):
    if not instance.title:
        print('nope')
        instance.title = List.get_list_title()


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
