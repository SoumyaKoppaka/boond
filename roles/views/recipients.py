from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views import generic

from ..decorators import recipient_required
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


@method_decorator([login_required, recipient_required], name='dispatch')
class RecipientHomeView(generic.TemplateView):
    template_name = 'roles/recipients/recipient_home.html'
