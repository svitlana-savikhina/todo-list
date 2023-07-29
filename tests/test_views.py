from datetime import datetime, timedelta

from django.test import TestCase
from django.urls import reverse

from tasks.models import Tag, Task


class TaskViewsTest(TestCase):
    def setUp(self):
        self.tags = Tag.objects.create(name="Test Tag")
        self.task = Task.objects.create(
            content="Test Task",
            deadline_time=datetime.now() + timedelta(hours=3),
            is_done=False,
        )
        self.task.tags.add(self.tags)

    def create_task_data(self, content, created_time, deadline_time, is_done=False):
        return {
            "content": content,
            "created_time": created_time,
            "deadline_time": deadline_time,
            "is_done": is_done,
            "tags": [self.tags.pk],
        }

    def test_task_list_view(self):
        url = reverse("tasks:index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.content)

    def test_task_update_view(self):
        url = reverse("tasks:task-update", args=[self.task.pk])
        form_data = self.create_task_data(
            "Updated Task", "2023-07-28 12:00:00", "2023-07-28 15:00:00"
        )
        response = self.client.post(url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, "Updated Task")

    def test_task_delete_view(self):
        url = reverse("tasks:task-delete", args=[self.task.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)

    def test_task_change_status_get(self):
        url = reverse("tasks:task-change-status", args=[self.task.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertTrue(self.task.is_done)


def create_tag_data(name):
    return {
        "name": name,
    }


class TagViewsTest(TestCase):
    def setUp(self):
        self.tags = Tag.objects.create(name="Test Tag")

    def create_tag_data(self):
        return {
            "name": self,
        }

    def test_tag_list_view(self):
        url = reverse("tasks:tag-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tags.name)

    def test_tag_create_view(self):
        url = reverse("tasks:tag-create")
        form_data = create_tag_data("New Tag")
        response = self.client.post(url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 2)

    def test_tag_update_view(self):
        url = reverse("tasks:tag-update", args=[self.tags.pk])
        form_data = create_tag_data("Updated Tag")
        response = self.client.post(url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.tags.refresh_from_db()
        self.assertEqual(self.tags.name, "Updated Tag")

    def test_tag_delete_view(self):
        url = reverse("tasks:tag-delete", args=[self.tags.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Tag.objects.count(), 0)
