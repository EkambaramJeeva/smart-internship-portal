from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegistrationForm, StudentProfileForm, CompanyProfileForm
from .models import UserProfile, StudentProfile
def register(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            role = form.cleaned_data['role']

            UserProfile.objects.create(
                user=user,
                role=role
            )

            return redirect('login')

    else:
        form = RegistrationForm()

    return render(request, 'accounts/register.html', {
        'form': form
    })


def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            profile = UserProfile.objects.get(user=user)

            if profile.role == 'student':
                return redirect('student_dashboard')

            elif profile.role == 'company':
                return redirect('company_dashboard')

        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'accounts/login.html')


def student_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')

    profile = UserProfile.objects.get(
        user=request.user
    )

    if profile.role != 'student':
        return redirect('login')

    from applications.models import Application
    from notifications.models import Notification

    application_count = Application.objects.filter(
        student=request.user
    ).count()

    shortlisted_count = Application.objects.filter(
        student=request.user,
        status='shortlisted'
    ).count()

    rejected_count = Application.objects.filter(
        student=request.user,
        status='rejected'
    ).count()

    notification_count = Notification.objects.filter(
        user=request.user,
        is_read=False
    ).count()

    return render(
        request,
        'accounts/student_dashboard.html',
        {
            'application_count': application_count,
            'shortlisted_count': shortlisted_count,
            'rejected_count': rejected_count,
            'notification_count': notification_count
        }
    )


def student_profile(request):

    if not request.user.is_authenticated:
        return redirect('login')

    profile = UserProfile.objects.get(user=request.user)

    if profile.role != 'student':
        return redirect('login')

    try:
        student_profile = StudentProfile.objects.get(
            user=request.user
        )
    except StudentProfile.DoesNotExist:
        student_profile = None

    if request.method == 'POST':

        if student_profile:
            form = StudentProfileForm(
                request.POST,
                request.FILES,
                instance=student_profile
            )
        else:
            form = StudentProfileForm(
                request.POST,
                request.FILES
            )

        if form.is_valid():

            student_profile = form.save(commit=False)

            student_profile.user = request.user

            student_profile.save()

            return redirect('student_dashboard')

    else:

        if student_profile:
            form = StudentProfileForm(
                instance=student_profile
            )
        else:
            form = StudentProfileForm()

    return render(
        request,
        'accounts/student_profile.html',
        {
            'form': form
        }
    )


def company_profile(request):

    if not request.user.is_authenticated:
        return redirect('login')

    profile = UserProfile.objects.get(
        user=request.user
    )

    if profile.role != 'company':
        return redirect('login')

    from .models import CompanyProfile

    try:
        company_profile = CompanyProfile.objects.get(
            user=request.user
        )
    except CompanyProfile.DoesNotExist:
        company_profile = None

    if request.method == 'POST':

        if company_profile:

            form = CompanyProfileForm(
                request.POST,
                instance=company_profile
            )

        else:

            form = CompanyProfileForm(
                request.POST
            )

        if form.is_valid():

            company_profile = form.save(
                commit=False
            )

            company_profile.user = request.user

            company_profile.save()

            return redirect('company_dashboard')

    else:

        if company_profile:

            form = CompanyProfileForm(
                instance=company_profile
            )

        else:

            form = CompanyProfileForm()

    return render(
        request,
        'accounts/company_profile.html',
        {
            'form': form
        }
    )



def view_company_profile(request):

    if not request.user.is_authenticated:
        return redirect('login')

    profile = UserProfile.objects.get(
        user=request.user
    )

    if profile.role != 'company':
        return redirect('login')

    from .models import CompanyProfile

    try:
        company_profile = CompanyProfile.objects.get(
            user=request.user
        )
    except CompanyProfile.DoesNotExist:
        return redirect('company_profile')

    return render(
        request,
        'accounts/view_company_profile.html',
        {
            'company_profile': company_profile
        }
    )


def company_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')

    profile = UserProfile.objects.get(
        user=request.user
    )

    if profile.role != 'company':
        return redirect('login')

    from applications.models import Application

    application_count = Application.objects.filter(
        internship__company=request.user
    ).count()

    shortlisted_count = Application.objects.filter(
        internship__company=request.user,
        status='shortlisted'
    ).count()

    rejected_count = Application.objects.filter(
        internship__company=request.user,
        status='rejected'
    ).count()

    return render(
        request,
        'accounts/company_dashboard.html',
        {
            'application_count': application_count,
            'shortlisted_count': shortlisted_count,
            'rejected_count': rejected_count
        }
    )


def user_logout(request):

    logout(request)

    return redirect('login')


def view_student_profile(request):

    if not request.user.is_authenticated:
        return redirect('login')

    profile = UserProfile.objects.get(user=request.user)

    if profile.role != 'student':
        return redirect('login')

    try:
        student_profile = StudentProfile.objects.get(
            user=request.user
        )
    except StudentProfile.DoesNotExist:
        return redirect('student_profile')

    return render(
        request,
        'accounts/view_student_profile.html',
        {
            'student_profile': student_profile
        }
    )