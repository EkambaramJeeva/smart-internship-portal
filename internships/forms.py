from django import forms
from .models import Internship


class InternshipForm(forms.ModelForm):

    class Meta:
        model = Internship

        fields = [
            'title',
            'description',
            'required_skills',
            'location',
            'duration',
            'stipend',
            'application_deadline'
        ]

        widgets = {
            'application_deadline': forms.DateInput(
                attrs={'type': 'date'}
            ),
        }