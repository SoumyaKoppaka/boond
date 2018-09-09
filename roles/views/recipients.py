from django.contrib.auth import login
from django.shortcuts import redirect
from django.views import generic

from ..forms import RecipientSignUpForm
from ..models import User


class RecipientSignUpView(generic.CreateView):
    model = User
    form_class = RecipientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'recipient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('recipient:recipient_home')


class RecipientHomeView(generic.TemplateView):
    template_name = 'roles/recipients/recipient_home.html'
