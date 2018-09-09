from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from roles.models import User, Donor, Recipient, BloodBank, Hospital, LocalBodies


class DonorSignUpForm(UserCreationForm):
    address = forms.CharField(
        widget=forms.TextInput,
        required=True,
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 1
        user.save()
        donor = Donor.objects.create(user=user)
        donor.address()
        donor.save()
        return user


class RecipientSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2
        user.save()
        recipient = Recipient.objects.create(user=user)
        recipient.save()
        return user


class BloodBankSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 3
        user.save()
        blood_bank = BloodBank.objects.create(user=user)
        blood_bank.save()
        return user


class HospitalSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 4
        user.save()
        hospital = Hospital.objects.create(user=user)
        hospital.save()
        return user


class LocalBodySignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 5
        user.save()
        local_body = LocalBodies.objects.create(user=user)
        local_body.save()
        return user
