from django.urls import path
from . import views


urlpatterns = [

    path(
        'post/',
        views.post_internship,
        name='post_internship'
    ),

    path(
        'my-internships/',
        views.my_internships,
        name='my_internships'
    ),

    path(
        'available/',
        views.available_internships,
        name='available_internships'
    ),

    path(
        'recommended/',
        views.recommended_internships,
        name='recommended_internships'
    ),

]