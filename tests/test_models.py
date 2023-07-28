from datetime import datetime, timedelta

from django.test import TestCase
from django.urls import reverse

from tasks.forms import TaskForm, TagForm
from tasks.models import Task, Tag


class ModelTest(TestCase):
    def test_task_str(self):
        task_ = Task.objects.create(
            content="test",
            created_time="2023-07-12 12:00",
            is_done=False,
            deadline_time="2023-07-13 12:00",
        )
        tag = Tag.objects.create(name="home")
        task_.tag.set([tag])
        self.assertEqual(
            str(task_),
            f"{task_.content} {task_.created_time} {task_.is_done} {task_.deadline_time} {task_.tag}",
        )

    def test_tag_str(self):
        name_ = Tag.objects.create(name="test")
        self.assertEqual(str(name_), name_.name)
