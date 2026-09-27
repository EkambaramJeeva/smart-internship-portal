from django import forms
from django.contrib.auth.models import User

from .models import UserProfile, StudentProfile, CompanyProfile


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    role = forms.ChoiceField(
        choices=UserProfile.ROLE_CHOICES
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password',
            'role'
        ]


class StudentProfileForm(forms.ModelForm):

    class Meta:
        model = StudentProfile

        fields = [
            'full_name',
            'phone',
            'education',
            'skills',
            'location',
            'resume',
            'internship_interests'
        ]


class CompanyProfileForm(forms.ModelForm):

    class Meta:
        model = CompanyProfile

        fields = [
            'company_name',
            'phone',
            'description',
            'location',
            'website'
        ]