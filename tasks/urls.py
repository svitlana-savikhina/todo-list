
from django.urls import path

from tasks.views import TodoListView, TaskCreateView

urlpatterns = [
    path("", TodoListView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
]

app_name = "tasks"
