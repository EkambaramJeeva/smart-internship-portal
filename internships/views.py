from django.shortcuts import render, redirect
from django.db.models import Q

from accounts.models import UserProfile
from .forms import InternshipForm
from .models import Internship


def post_internship(request):

    if not request.user.is_authenticated:
        return redirect('login')

    profile = UserProfile.objects.get(user=request.user)

    if profile.role != 'company':
        return redirect('login')

    if request.method == 'POST':

        form = InternshipForm(request.POST)

        if form.is_valid():

            internship = form.save(commit=False)

            internship.company = request.user

            internship.save()

            return redirect('company_dashboard')

    else:
        form = InternshipForm()

    return render(
        request,
        'internships/post_internship.html',
        {
            'form': form
        }
    )


def my_internships(request):

    if not request.user.is_authenticated:
        return redirect('login')

    profile = UserProfile.objects.get(user=request.user)

    if profile.role != 'company':
        return redirect('login')

    internships = Internship.objects.filter(
        company=request.user
    )

    return render(
        request,
        'internships/my_internships.html',
        {
            'internships': internships
        }
    )


def available_internships(request):

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

    search = request.GET.get('search', '')
    location = request.GET.get('location', '')

    internships = Internship.objects.all().order_by(
        '-created_at'
    )

    if search:
     internships = internships.filter(
        Q(title__icontains=search) |
        Q(required_skills__icontains=search)
    )

    if location:
        internships = internships.filter(
            location__icontains=location
        )

    return render(
        request,
        'internships/available_internships.html',
        {
            'internships': internships,
            'search': search,
            'location': location
        }
    )


def recommended_internships(request):

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

    from accounts.models import StudentProfile

    try:
        student_profile = StudentProfile.objects.get(
            user=request.user
        )
    except StudentProfile.DoesNotExist:
        return redirect('student_profile')

    student_skills = [
        skill.strip().lower()
        for skill in student_profile.skills.split(',')
    ]

    internships = Internship.objects.all()

    recommended = []

    for internship in internships:

        required_skills = [
            skill.strip().lower()
            for skill in internship.required_skills.split(',')
        ]

        matching_skills = []

        for skill in student_skills:

            if skill in required_skills:
                matching_skills.append(skill)

        if matching_skills:

            match_percentage = (
                len(matching_skills)
                / len(required_skills)
            ) * 100

            recommended.append({
                'internship': internship,
                'matching_skills': matching_skills,
                'match_count': len(matching_skills),
                'match_percentage': round(
                    match_percentage
                )
            })

    recommended.sort(
        key=lambda x: x['match_percentage'],
        reverse=True
    )

    return render(
        request,
        'internships/recommended_internships.html',
        {
            'recommended': recommended
        }
    )