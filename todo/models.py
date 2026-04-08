# todo/models.py
from django.db import models

class ToDoItem2(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    class Meta:
        db_table = 'ToDoItem2'  # ← ここでテーブル名を直接指定！
    def __str__(self):
        return self.title
