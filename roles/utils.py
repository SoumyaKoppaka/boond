from django.conf import settings
from django.core.mail import send_mail

from .models import User


def send_event_message():
    recipients = []
    for user in User.objects.all():
        if not user.user_type == 6:
            recipients.append(user.email)
    send_mail(
        subject='Blood Donation Event',
        message=
        'A new Blood Donation Event is being organized.\nPlease visit the site to view it.',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipients,
    )