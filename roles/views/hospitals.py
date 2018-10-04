from django.contrib.auth import login
from django.shortcuts import redirect
from django.views import generic

from ..forms import HospitalSignUpForm
from ..models import User


class HospitalSignUpView(generic.CreateView):
    model = User
    form_class = HospitalSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 4
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('hospital:hospital_home')


class HospitalHomeView(generic.TemplateView):
    template_name = 'roles/hospitals/hospital_home.html'
