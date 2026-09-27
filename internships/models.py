from django.db import models
from django.contrib.auth.models import User


class Internship(models.Model):

    company = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    required_skills = models.TextField()

    location = models.CharField(
        max_length=100
    )

    duration = models.CharField(
        max_length=100
    )

    stipend = models.CharField(
        max_length=100
    )

    application_deadline = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title