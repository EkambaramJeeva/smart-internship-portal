from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'message',
        'is_read',
        'created_at',
    )

    search_fields = (
        'user__username',
        'user__email',
        'message',
    )

    list_filter = (
        'is_read',
        'created_at',
    )

    ordering = (
        '-created_at',
    )