from django.conf import settings
from django.core.mail import EmailMessage


def create_email_message(subject, message, recipient_list):
    return EmailMessage(subject=subject, body=message, from_email=settings.EMAIL_HOST_USER, to=recipient_list)
