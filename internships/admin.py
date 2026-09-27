from django.contrib import admin

from .models import Internship


@admin.register(Internship)
class InternshipAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'company',
        'location',
        'duration',
        'stipend',
        'application_deadline',
        'created_at',
    )

    search_fields = (
        'title',
        'required_skills',
        'location',
        'company__username',
    )

    list_filter = (
        'location',
        'application_deadline',
        'created_at',
    )

    ordering = (
        '-created_at',
    )