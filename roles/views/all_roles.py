from django.shortcuts import render
from django.views import generic

def home(request):
    return render(request, 'roles/home.html')


class SignUpView(generic.TemplateView):
    template_name = 'register.html'
