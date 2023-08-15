from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskList(admin.ModelAdmin):
    list_display = ('id','user', 'title', 'description', 'due_date', 'completion')