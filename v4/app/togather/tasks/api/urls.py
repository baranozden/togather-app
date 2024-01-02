from django.urls import path
from . import views

urlpatterns = [
    path('tasks', views.TaskView.as_view(), name='tasks'),
    path('addtask', views.AddTaskView.as_view(), name='addtask')
]