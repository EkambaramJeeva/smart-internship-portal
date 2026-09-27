from django.db import models
from django.contrib.auth.models import User
from internships.models import Internship


class Application(models.Model):

    STATUS_CHOICES = (
        ('applied', 'Applied'),
        ('shortlisted', 'Shortlisted'),
        ('rejected', 'Rejected'),
    )

    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    internship = models.ForeignKey(
        Internship,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='applied'
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student.username} - {self.internship.title}"