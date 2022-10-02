from django.db import models
from usersapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=150, unique=True)
    repo = models.URLField()
    users = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Todo(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    updated = models.DateTimeField(auto_now=True, verbose_name="Edited")
    deleted = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.project} {self.creator} {self.created}'
