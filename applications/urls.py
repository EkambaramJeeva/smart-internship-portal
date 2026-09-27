from django.urls import path
from . import views


urlpatterns = [

    path(
        'apply/<int:internship_id>/',
        views.apply_internship,
        name='apply_internship'
    ),

    path(
        'my-applications/',
        views.my_applications,
        name='my_applications'
    ),

    path(
        'company-applications/<int:internship_id>/',
        views.company_applications,
        name='company_applications'
    ),

    path(
        'update-status/<int:application_id>/<str:status>/',
        views.update_application_status,
        name='update_application_status'
    ),

]