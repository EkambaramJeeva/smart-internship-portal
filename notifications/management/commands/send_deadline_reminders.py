from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from internships.models import Internship
from applications.models import Application
from notifications.models import Notification


class Command(BaseCommand):

    help = 'Send internship deadline reminders'

    def handle(self, *args, **kwargs):

        today = timezone.now().date()

        reminder_date = today + timedelta(days=3)

        internships = Internship.objects.filter(
            application_deadline=reminder_date
        )

        for internship in internships:

            applications = Application.objects.filter(
                internship=internship
            )

            for application in applications:

                Notification.objects.create(
                    user=application.student,
                    message=(
                        f'Reminder: The application deadline for '
                        f'{internship.title} is in 3 days.'
                    )
                )

        self.stdout.write(
            self.style.SUCCESS(
                'Deadline reminders sent successfully.'
            )
        )