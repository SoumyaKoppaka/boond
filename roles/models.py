from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Donor'),
        (2, 'Recipient'),
        (3, 'BloodBank'),
        (4, 'Hospital'),
        (5, 'LocalBody'),
        (6, 'Admin'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    name = models.CharField(max_length=50)


class Donor(models.Model):
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=40, default='')
    location = models.CharField(max_length=40, default='')
    email_address = models.EmailField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Recipient(models.Model):
    first_name = models.CharField(max_length=40, default='')
    last_name = models.CharField(max_length=40, default='')
    location = models.CharField(max_length=40, default='')
    email_address = models.EmailField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class BloodBank(models.Model):
    name = models.CharField(max_length=40, default='')
    location = models.CharField(max_length=40, default='')
    email_address = models.EmailField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Hospital(models.Model):
    name = models.CharField(max_length=40, default='')
    location = models.CharField(max_length=40, default='')
    email_address = models.EmailField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class LocalBodies(models.Model):
    name = models.CharField(max_length=40, default='')
    location = models.CharField(max_length=40, default='')
    email_address = models.EmailField(default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


"""
@receiver(post_save, sender=User)
def create_user_type_object(sender, instance, created, **kwargs):
    if created:
        obj = User(instance)
        if obj.user_type == 1:
            Donor.objects.create(user=obj)
        elif obj.user_type == 2:
            Recipient.objects.create(user=obj)
        elif obj.user_type == 3:
            BloodBank.objects.create(user=obj)
        elif obj.user_type == 4:
            Hospital.objects.create(user=obj)
        elif obj.user_type == 5:
            BloodBank.objects.create(user=obj)

@receiver(post_save, sender=User)
def save_user_type_object(sender, instance, **kwargs):
    obj = User(instance)
    # if(obj.user_type == 1):
    
"""


class BloodDonationEvent(models.Model):
    user = models.ForeignKey(User, default=5, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    organizer = models.CharField(max_length=50)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    # time = models.TimeField()
    poster = models.FileField()
    status = models.IntegerField(default=0)

    def __str__(self):
        return self.organizer + ' - ' + self.location
