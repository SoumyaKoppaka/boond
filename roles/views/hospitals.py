from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import generic

from ..decorators import hospital_required
from ..forms import HospitalSignUpForm, ReserveForm
from ..models import User, Blood, Request
from ..utils import send_confirmation_recipient_message, send_request_donor_message


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


@hospital_required
def reserve_blood(request):
    # if not request.user.is_authenticated:
    # return render(request, 'registration/signup_form.html')
    # else:
    form = ReserveForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        event = form.save(commit=True)
        event.user = request.user

    # return render(request, 'roles/loLocal Bodies:cal_bodies/local_bodies_home.html', {'event': event})
    context = {
        "form": form,

    }
    return render(request, 'roles/hospitals/reserve_blood.html', context)


@hospital_required
def search(request):
    # search_query = request.GET.get('name')
    a = Request.objects.latest('time')

    search_query = a.request_type
    try:
        results = Blood.objects.filter(blood_type__icontains=search_query)
    except Blood.DoesNotExist:
        results = None
    context = {
        'search_query': search_query,
        'results': results
    }
    return render(request, 'roles/hospitals/search.html', context)


@hospital_required
def block_blood(request, slug):
    if request.method == "GET":
        blocked_blood = Blood.objects.get(slug=slug)
        blocked_blood.status = 1
        print(blocked_blood)
        blocked_blood.save()
        send_confirmation_recipient_message(blocked_blood)

        # quantity = int(request.POST.get('qty')) or 1

        # return redirect(reversetime('view_cart'))
        # return render(request,'roles/hospitals/search.html',{} )
        return render(request, 'roles/hospitals/detail.html', {'product': blocked_blood})
    return render(request, 'roles/hospitals/search.html', {})


@method_decorator([login_required, hospital_required], name='dispatch')
class HospitalHomeView(generic.TemplateView):
    template_name = 'roles/hospitals/hospital_home.html'


@hospital_required
def send_email_reserve_conf(request, slug):
    if request.method == "GET":
        # cart = get_user_cart(request)
        blocked_blood = Blood.objects.get(blood_type=slug)
        send_confirmation_recipient_message(blocked_blood)


@hospital_required
def send_email_request(request, slug):
    if request.method == "GET":
        # cart = get_user_cart(request)
        blocked_blood = Blood.objects.get(blood_type=slug)
        print(blocked_blood)
        send_request_donor_message(blocked_blood)

    # Send email to donors of the particular blood type


'''
def run_continuously(self, interval=1):
    """Continuously run, while executing pending jobs at each elapsed
    time interval.
    @return cease_continuous_run: threading.Event which can be set to
    cease continuous run.
    Please note that it is *intended behavior that run_continuously()
    does not run missed jobs*. For example, if you've registered a job
    that should run every minute and you set a continuous run interval
    of one hour then your job won't be run 60 times at each interval but
    only once.
    """

    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):

        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                self.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.setDaemon(True)
    continuous_thread.start()
    return cease_continuous_run


Scheduler.run_continuously = run_continuously

'''
