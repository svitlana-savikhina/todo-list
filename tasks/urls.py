
from django.urls import path

from tasks.views import (
    TodoListView,
    TaskCreateView,
    TaskUpdateView, TaskDeleteView
)

urlpatterns = [
    path("", TodoListView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),

]

app_name = "tasks"
