from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic

from ..decorators import blood_bank_required
from ..forms import BloodBankSignUpForm
from ..models import User


class BloodBankSignUpView(generic.CreateView):
    model = User
    form_class = BloodBankSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 3
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('blood_bank:blood_bank_home')


@method_decorator([login_required, blood_bank_required], name='dispatch')
class BloodBankHomeView(generic.TemplateView):
    template_name = 'roles/blood_banks/blood_bank_home.html'
