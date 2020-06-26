from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

from accounts.models import CustomUserModel, UserModel1
# Create your views here.


class SignUpView(TemplateView):
	template_name 		= 'registration/signup.html'



class Profile(DetailView):
	model 				= CustomUserModel
	context_object_name = 'profile'
	slug_field 			= 'slug'
	slug_url_kwargs 	= 'slug'
	template_name 		= 'accounts/um1_profile.html'


	def get_context_data(self, **kwargs):
		context 	= super().get_context_data(**kwargs)

		#Dynamically get slug for logged in user
		u_slug 		= self.kwargs.get('slug')

		#Get all the object for the logged in user
		obj 		= CustomUserModel.objects.get(slug=u_slug)

		# to get user id 
		get_id 		= obj.u_id

		#to get the extra added objects
		um1_extra_obj 		= UserModel1.objects.filter(user_id=get_id)

		context['um1_extra_obj'] = um1_extra_obj


		return context



