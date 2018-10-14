from django import forms
from django.contrib.auth.forms import UserCreationForm

from roles.models import User, Donor, Recipient, BloodBank, Hospital, LocalBodies, BloodDonationEvent


class DonorSignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput,
        required=True
    )

    last_name = forms.CharField(
        widget=forms.TextInput,
        required=True
    )

    location = forms.CharField(
        widget=forms.TextInput,
        required=True,
    )

    email_address = forms.EmailField(
        widget=forms.TextInput,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 1
        user.save()
        donor = Donor.objects.create(user=user)
        donor.location = self.cleaned_data.get('location')
        donor.first_name = self.cleaned_data.get('first_name')
        donor.last_name = self.cleaned_data.get('last_name')
        donor.email_address = self.cleaned_data.get('email_address')
        donor.save()
        return user


class RecipientSignUpForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput,
        required=True
    )

    last_name = forms.CharField(
        widget=forms.TextInput,
        required=True
    )

    location = forms.CharField(
        widget=forms.TextInput,
        required=True,
    )

    email_address = forms.EmailField(
        widget=forms.TextInput,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2
        user.save()
        recipient = Recipient.objects.create(user=user)
        recipient.first_name = self.cleaned_data.get('first_name')
        recipient.last_name = self.cleaned_data.get('last_name')
        recipient.location = self.cleaned_data.get('location')
        recipient.email_address = self.cleaned_data.get('email_address')
        recipient.save()
        return user


class BloodBankSignUpForm(UserCreationForm):
    name = forms.CharField(
        widget=forms.TextInput,
        required=True
    )

    location = forms.CharField(
        widget=forms.TextInput,
        required=True,
    )

    email_address = forms.EmailField(
        widget=forms.TextInput,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 3
        user.save()
        blood_bank = BloodBank.objects.create(user=user)
        blood_bank.name = self.cleaned_data.get('name')
        blood_bank.location = self.cleaned_data.get('location')
        blood_bank.email_address = self.cleaned_data.get('email_address')
        blood_bank.save()
        return user


class HospitalSignUpForm(UserCreationForm):
    name = forms.CharField(
        widget=forms.TextInput,
        required=True
    )

    location = forms.CharField(
        widget=forms.TextInput,
        required=True,
    )

    email_address = forms.EmailField(
        widget=forms.TextInput,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 4
        user.save()
        hospital = Hospital.objects.create(user=user)
        hospital.name = self.cleaned_data.get('name')
        hospital.location = self.cleaned_data.get('location')
        hospital.email_address = self.cleaned_data.get('email_address')
        hospital.save()
        return user


class LocalBodySignUpForm(UserCreationForm):
    name = forms.CharField(
        widget=forms.TextInput,
        required=True
    )

    location = forms.CharField(
        widget=forms.TextInput,
        required=True,
    )

    email_address = forms.EmailField(
        widget=forms.TextInput,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 5
        user.save()
        local_body = LocalBodies.objects.create(user=user)
        local_body.name = self.cleaned_data.get('name')
        local_body.location = self.cleaned_data.get('location')
        local_body.email_address = self.cleaned_data.get('email_address')
        local_body.save()
        return user


class EventForm(forms.ModelForm):
    class Meta:
        model = BloodDonationEvent
        fields = ['name', 'organizer', 'location', 'date', 'description', 'poster']
