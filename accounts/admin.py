from django.contrib import admin

from .models import (
    UserProfile,
    StudentProfile,
    CompanyProfile
)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'role',
    )

    search_fields = (
        'user__username',
        'user__email',
    )

    list_filter = (
        'role',
    )


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'user',
        'education',
        'location',
        'internship_interests',
    )

    search_fields = (
        'full_name',
        'user__username',
        'user__email',
        'education',
        'skills',
        'location',
    )

    list_filter = (
        'education',
        'location',
    )


@admin.register(CompanyProfile)
class CompanyProfileAdmin(admin.ModelAdmin):

    list_display = (
        'company_name',
        'user',
        'phone',
        'location',
        'website',
    )

    search_fields = (
        'company_name',
        'user__username',
        'user__email',
        'location',
    )

    list_filter = (
        'location',
    )