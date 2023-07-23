
from django.urls import path

from tasks.views import (
    TodoListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TaskChangeStatusView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="index"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tasks/<int:pk>/change-status/", TaskChangeStatusView.as_view(), name="task-change-status"),

]

app_name = "tasks"
