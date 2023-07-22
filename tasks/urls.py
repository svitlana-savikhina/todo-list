from django.urls import path

from tasks.views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="index"),
]

app_name = "tasks"
