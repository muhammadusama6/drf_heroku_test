from django.db import models


class TestApi(models.Model):
    rollNum = models.TextField(default='')
