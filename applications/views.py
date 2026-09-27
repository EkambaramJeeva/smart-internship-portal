from django.shortcuts import render, redirect
from django.contrib import messages

from accounts.models import UserProfile
from internships.models import Internship
from notifications.models import Notification

from .models import Application

def apply_internship(request, internship_id):

    if not request.user.is_authenticated:
        return redirect('login')

    profile = UserProfile.objects.get(
        user=request.user
    )

    if profile.role != 'student':
        return redirect('login')

    internship = Internship.objects.get(
        id=internship_id
    )

    existing_application = Application.objects.filter(
        student=request.user,
        internship=internship
    ).first()

    if existing_application:
        messages.warning(
            request,
            'You have already applied for this internship.'
        )

        return redirect('available_internships')

    Application.objects.create(
        student=request.user,
        internship=internship
    )

    messages.success(
        request,
        'Application submitted successfully!'
    )

    return redirect('available_internships')



def my_applications(request):

    if not request.user.is_authenticated:
        return redirect('login')

    try:
        profile = UserProfile.objects.get(
            user=request.user
        )
    except UserProfile.DoesNotExist:
        return redirect('login')

    if profile.role != 'student':
        return redirect('login')

    applications = Application.objects.filter(
        student=request.user
    ).select_related('internship')

    return render(
        request,
        'applications/my_applications.html',
        {
            'applications': applications
        }
    )



def company_applications(request, internship_id):

    if not request.user.is_authenticated:
        return redirect('login')

    try:
        profile = UserProfile.objects.get(
            user=request.user
        )
    except UserProfile.DoesNotExist:
        return redirect('login')

    if profile.role != 'company':
        return redirect('login')

    internship = Internship.objects.get(
        id=internship_id
    )

    if internship.company != request.user:
        return redirect('company_dashboard')

    applications = Application.objects.filter(
    internship=internship
).select_related(
    'student',
    'student__studentprofile'
)
    return render(
        request,
        'applications/company_applications.html',
        {
            'internship': internship,
            'applications': applications
        }
    )


def update_application_status(request, application_id, status):

    if not request.user.is_authenticated:
        return redirect('login')

    try:
        profile = UserProfile.objects.get(
            user=request.user
        )
    except UserProfile.DoesNotExist:
        return redirect('login')

    if profile.role != 'company':
        return redirect('login')

    application = Application.objects.get(
        id=application_id
    )

    if application.internship.company != request.user:
        return redirect('company_dashboard')

    if status in ['shortlisted', 'rejected']:

     if application.status == status:
        return redirect(
            'company_applications',
            application.internship.id
        )

    application.status = status
    application.save()
    if status == 'shortlisted':

            message = (
                f'Your application for '
                f'{application.internship.title} '
                f'has been shortlisted.'
            )

    else:

            message = (
                f'Your application for '
                f'{application.internship.title} '
                f'has been rejected.'
            )

    Notification.objects.create(
            user=application.student,
            message=message
        )

    return redirect(
        'company_applications',
        application.internship.id
    )