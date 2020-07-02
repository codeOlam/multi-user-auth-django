from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from accounts.models import Users, UserTypeA, UserTypeB
# Create your views here.


class SignUpView(TemplateView):
	template_name 		= 'registration/signup.html'