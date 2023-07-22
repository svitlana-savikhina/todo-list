from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    deadline_time = models.DateTimeField()
    is_done = models.BooleanField()
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ["is_done", "-created_time"]

    def __str__(self):
        return f"{self.content} {self.created_time} {self.is_done} {self.tags}"
