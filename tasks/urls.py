
from django.urls import path

from tasks.views import (
    TodoListView,
    TaskCreateView,
    TaskUpdateView
)

urlpatterns = [
    path("", TodoListView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),

]

app_name = "tasks"
