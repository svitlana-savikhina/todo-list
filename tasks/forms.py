from django import forms

from tasks.models import Task, Tag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ("content", "deadline_time", "is_done", "tags",)
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
            "deadline_time": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"
