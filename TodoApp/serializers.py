from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        task = Task(
            user = user,
            title = self.validated_data['title'],
            description = self.validated_data['description'],
            completion = self.validated_data['completion'],
            due_date = self.validated_data['due_date']
        )
     
        task.save()
        return task
