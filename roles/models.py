from django.contrib.auth.models import AbstractUser
from django.db import models


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

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=5)
    name = models.CharField(max_length=50)


class Donor(models.Model):
    address = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Recipient(models.Model):
    address = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class BloodBank(models.Model):
    address = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class Hospital(models.Model):
    address = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


class LocalBodies(models.Model):
    address = models.CharField(max_length=300)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username

class BloodDonationEvent(models.Model):
    user = models.ForeignKey(User, default=5, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    organizer = models.CharField(max_length=50)
    date=models.DateTimeField()
    location=models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    #time=models.TimeField()
    poster = models.FileField()
    status=models.IntegerField(default=0)


    def __str__(self):
        return self.organizer + ' - ' + self.location
