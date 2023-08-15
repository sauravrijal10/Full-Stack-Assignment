from django.shortcuts import render
from rest_framework import generics
from .serializers import TaskSerializer
from .models import Task

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        # Only show tasks for the currently logged-in user
        return Task.objects.filter(user=self.request.user)

class TaskRetriveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

