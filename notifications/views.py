from django.shortcuts import render, redirect
from .models import Notification


def notification_list(request):

    if not request.user.is_authenticated:
        return redirect('login')

    notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')

    Notification.objects.filter(
        user=request.user,
        is_read=False
    ).update(
        is_read=True
    )

    return render(
        request,
        'notifications/notification_list.html',
        {
            'notifications': notifications
        }
    )