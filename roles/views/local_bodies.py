from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import generic

from ..forms import LocalBodySignUpForm, EventForm
from ..models import User, BloodDonationEvent

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


class LocalBodySignUpView(generic.CreateView):
    model = User
    form_class = LocalBodySignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 5
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('local_bodies:local_bodies_home')


class LocalBodyHomeView(generic.TemplateView):
    template_name = 'roles/local_bodies/local_bodies_home.html'


def view_event(request):
    all_products = BloodDonationEvent.objects.all()
    return render(request, 'roles/local_bodies/all_events.html', {'all_products': all_products})


def upload_event(request):
    # if not request.user.is_authenticated:
    # return render(request, 'registration/signup_form.html')
    # else:
    form = EventForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        event = form.save(commit=False)
        event.user = request.user

        event.poster = request.FILES['poster']
        file_type = event.poster.url.split('.')[-1]
        file_type = file_type.lower()
        if file_type not in IMAGE_FILE_TYPES:
            context = {
                'event': event,
                'form': form,
                'error_message': 'Image file must be PNG, JPG, or JPEG',
            }
            event.save()
            return render(request, 'roles/local_bodies/upload_event.html', context)
        event.save()
        return render(request, 'roles/local_bodies/local_bodies_home.html', {'event': event})
    context = {
        "form": form,
    }
    return render(request, 'roles/local_bodies/upload_event.html', context)
