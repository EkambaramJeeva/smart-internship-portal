from django.urls import path
from . import views


urlpatterns = [

    path(
        'register/',
        views.register,
        name='register'
    ),

    path(
        'login/',
        views.user_login,
        name='login'
    ),

    path(
        'student-dashboard/',
        views.student_dashboard,
        name='student_dashboard'
    ),

    path(
        'company-dashboard/',
        views.company_dashboard,
        name='company_dashboard'
    ),

    path(
        'student-profile/',
        views.student_profile,
        name='student_profile'
    ),

    path(
        'view-profile/',
        views.view_student_profile,
        name='view_student_profile'
    ),


    path(
    'company-profile/',
    views.company_profile,
    name='company_profile'
),



   path(
    'company-profile/',
    views.company_profile,
    name='company_profile'
),

path(
    'view-company-profile/',
    views.view_company_profile,
    name='view_company_profile'
),

path(
    'logout/',
    views.user_logout,
    name='logout'
),

]