from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):

    ROLE_CHOICES = (
        ('student', 'Student'),
        ('company', 'Company'),
    )

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    def __str__(self):
        return self.user.username


class StudentProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=15
    )

    education = models.CharField(
        max_length=200
    )

    skills = models.TextField()

    location = models.CharField(
        max_length=100
    )

    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )

    internship_interests = models.CharField(
        max_length=200
    )

    def __str__(self):
        return self.full_name


class CompanyProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    company_name = models.CharField(
        max_length=150
    )

    phone = models.CharField(
        max_length=15
    )

    description = models.TextField()

    location = models.CharField(
        max_length=100
    )

    website = models.URLField(
        blank=True
    )

    def __str__(self):
        return self.company_name