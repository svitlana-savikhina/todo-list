from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "tag": forms.CheckboxSelectMultiple(),
            "created_time": forms.DateTimeInput(attrs={"type": "datetime-local"}),
            "deadline_time": forms.DateTimeInput(attrs={"type": "datetime-local"})
        }


