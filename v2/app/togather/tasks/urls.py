from django.urls import path, include
from .views import main, add_task, delete_task, show_tasks, update_task


urlpatterns = [
    path('home', main),
    path('', show_tasks, name="show_tasks"),
    path("add_task", add_task, name="add_task"),
    path("update_task/<str:pk>", update_task, name="update_task"),
    path("delete_task/<str:pk>", delete_task, name="delete_task")
]