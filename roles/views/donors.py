from django.contrib.auth import login
from django.shortcuts import redirect
from django.views import generic

from ..forms import DonorSignUpForm
from ..models import User


class DonorSignUpView(generic.CreateView):
    model = User
    form_class = DonorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 1
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('donor:donor_home')


class DonorHomeView(generic.TemplateView):
    template_name = 'roles/donors/donor_home.html'
