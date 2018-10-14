from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic

from ..decorators import hospital_required
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


@method_decorator([login_required, hospital_required], name='dispatch')
class HospitalHomeView(generic.TemplateView):
    template_name = 'roles/hospitals/hospital_home.html'
