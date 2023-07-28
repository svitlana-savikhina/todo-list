from unittest import TestCase

from tasks.forms import TagForm, TaskForm
from tasks.models import Tag


class FormsTests(TestCase):
    def test_tag_creation_forms(self):
        form_data = {"name": "test"}
        form = TagForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_task_form_creation(self):
        tag = Tag.objects.create(name="Test Tag")
        form_data = {
            "content": "Test",
            "created_time": "2023-07-28 12:00:00",
            "deadline_time": "2023-07-28 15:00:00",
            "is_done": False,
            "tag": [tag.pk],
        }

        form = TaskForm(data=form_data)
        self.assertTrue(form.is_valid())
