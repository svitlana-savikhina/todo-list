from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from tasks.forms import TaskForm, TagForm
from tasks.models import Task, Tag


class TodoListView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


class TaskChangeStatusView(View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("tasks:index")

    def post(self, request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = request.POST.get("is_done", not task.is_done)
        task.save()
        return redirect("tasks:index")


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag-list")
