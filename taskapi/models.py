from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=100, default='')
    is_checked = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
