from django.urls import path
from .views import TaskListCreateView, TaskRetriveUpdateDeleteView

app_name = 'TodoApp'

urlpatterns = [
    path('task/', TaskListCreateView.as_view(), name='Task_View'),
    path('task/<int:pk>/', TaskRetriveUpdateDeleteView.as_view(), name='Task_Views')
]

