from django.core.mail import send_mail

from .models import User


def send_event_message():
    recipients = []
    for user in User.objects.all():
        if not user.user_type == 6:
            recipients.append(user.email)
    send_mail(
        subject='Blood Donation Event',
        message='A new Blood Donation Event is being organized.\nPlease visit the site to view it.',
        from_email='Boond',
        recipient_list=recipients,
    )


def send_confirmation_recipient_message(recipient):
    recipients = []
    for user in recipient.user:
        recipients.append(user.email)
    send_mail(
        subject='Blood Blocking Confirmation',
        message='Blood has been reserved. Please collect it within 2 hours.',
        from_email='Boond',
        recipient_list=recipients,
    )


def send_update_reminder():
    recipients = []
    for user in User.objects.all():
        if user.user_type == 3 or user.user_type == 4:
            recipients.append(user.email)
    send_mail(
        subject='Blood Status update',
        message='Gentle reminder for periodic update of blood inventory.',
        from_email='Boond',
        recipient_list=recipients
    )


def send_request_donor_message(recipient):
    recipients = []
    for user in recipient.user:
        if user.user_type == 1:
            recipients.append(user.email)
    send_mail(
        subject='Blood Donation Request',
        message='Please donate blood',
        recipient_list=recipients
    )