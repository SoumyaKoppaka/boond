from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.views import generic

from ..forms import HospitalSignUpForm, ReserveForm
from ..models import User, Request, Blood,BloodBank


class HospitalSignUpView(generic.CreateView):
    model = User
    form_class = HospitalSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'hospital'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('hospital:hospital_home')


class HospitalHomeView(generic.TemplateView):
    template_name = 'roles/hospitals/hospital_home.html'

def reserve_blood(request):
    # if not request.user.is_authenticated:
    # return render(request, 'registration/signup_form.html')
    # else:
    form = ReserveForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        event = form.save(commit=True)
        event.user = request.user

       # return render(request, 'roles/local_bodies/local_bodies_home.html', {'event': event})
    context = {
        "form": form,


    }
    return render(request, 'roles/hospitals/reserve_blood.html', context)

def search(request):
    #search_query = request.GET.get('name')
    a=Request.objects.latest('time')

    search_query =a.request_type
    results = Blood.objects.filter(blood_type__icontains=search_query)
    context={
        'search_query':search_query,
        'results':results
    }
    return render(request,'roles/hospitals/search.html',context )

def block_blood(request, slug):
    if request.POST:
        #cart = get_user_cart(request)
        blocked_blood = Blood.objects.get(slug=slug)
        blocked_blood.status=1

        #quantity = int(request.POST.get('qty')) or 1

    #return redirect(reverse('view_cart'))
    #return render(request,'roles/hospitals/search.html',{} )
        return render(request, 'roles/hospitals/detail.html', {'product': blocked_blood})



