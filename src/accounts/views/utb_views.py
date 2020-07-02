from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, TemplateView
from django.urls import reverse_lazy, reverse 
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from accounts.models import Users, UserTypeB
from accounts.forms.utb_forms import UTBCreationForm, UTBChangeForm, UserUpdateForm


class SignUpUTBView(CreateView):
	form_class			= UTBCreationForm
	template_name 		= 'registration/utb_signup.html'
	success_url 		= reverse_lazy('login')


class UTBProfile(DetailView):
	model 				= Users
	context_object_name = 'profile'
	template_name 		= 'accounts/utb_profile.html'


	def get_context_data(self, **kwargs):
		context 	= super().get_context_data(**kwargs)

		#Dynamically get u_id for logged in user
		u_u_id 		= self.kwargs.get('pk')
		#Get all the object for the logged in user
		obj 		= Users.objects.get(u_id=u_u_id)
		# to get user id 
		get_id 		= obj.u_id
		#to get the extra added objects
		utb_extra_obj 		= UserTypeB.objects.filter(user_id=get_id)

		context['utb_extra_obj'] = utb_extra_obj


		return context


class UpdateUTBView(UpdateView):
	model 				= Users
	um1_model 			= UserTypeB
	form_class 			= UserUpdateForm
	um1_form_class 		= UTBChangeForm
	template_name 		= 'accounts/utb_update.html'


	def get_object(self, queryset=None):
		cum_obj 		= self.model.objects.get(u_id=self.kwargs.get('pk'))
		return cum_obj


	def post(self, request, *args, **kwargs):
		# getting objects of models
		cum_id 			= self.get_object().u_id
		um1_obj 		= self.um1_model.objects.filter(user_id=cum_id).first()

		# getting forms
		cum_form 		= self.form_class(request.POST, instance=self.get_object())
		um1_form 		= self.um1_form_class(request.POST, instance=um1_obj)


		if cum_form.is_valid() and um1_form.is_valid():
			cum_instance 				= cum_form.save(commit=False)
			cum_form 					= cum_instance.save()

			#For form UM1 form handling
			um1_instance 				= um1_form.save(commit=False)
			#get cleaned data from the POST form
			um1_cleaned_exec 			= um1_form.cleaned_data['exec_postion']
			um1_cleaned_level 			= um1_form.cleaned_data['level']
			#save update model
			um1_instance.exec_postion 	= um1_cleaned_exec
			um1_instance.level 			= um1_cleaned_level
			#save data to db
			um1_instance.user 			= cum_instance
			um1_instance.save()
			
			# return HttpResponseRedirect(reverse_lazy(self.get_success_url()))
			return HttpResponseRedirect('/')
		else:
			context = self.get_context_data(**kwargs)
			return TemplateResponse(request, self.template_name, context)
	

	def get_context_data(self, **kwargs):
		context 		= super().get_context_data(**kwargs)
		cum_id 			= self.get_object().u_id
		um1_obj 		= self.um1_model.objects.filter(user_id=cum_id).first()
		context['cum_form'] = self.form_class(instance=self.get_object())
		context['um1_form'] = self.um1_form_class(instance=um1_obj)
		return context

	def get_success_url(self):
		return reverse('accounts:utb_profile', kwargs={'pk': self.kwargs.get('pk')})