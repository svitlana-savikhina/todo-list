from django.test import TestCase

from tasks.models import Task, Tag


class ModelTest(TestCase):
    def test_task_str(self):
        task_ = Task.objects.create(
            content="test",
            created_time="2023-07-12 12:00",
            is_done=False,
            deadline_time="2023-07-13 12:00",
        )
        tags = Tag.objects.create(name="home")
        task_.tags.set([tags])
        self.assertEqual(
            str(task_),
            f"{task_.content} {task_.created_time} {task_.is_done} {task_.deadline_time} {task_.tags}",
        )

    def test_tag_str(self):
        name_ = Tag.objects.create(name="test")
        self.assertEqual(str(name_), name_.name)
