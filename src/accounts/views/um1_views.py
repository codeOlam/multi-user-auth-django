from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, TemplateView
from django.urls import reverse_lazy, reverse 
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

from accounts.models import CustomUserModel, UserModel1
from accounts.forms.um1_forms import UM1CreationForm, UM1ChangeForm, CustomeUserUpdateForm


class SignUpUm1View(CreateView):
	form_class			= UM1CreationForm
	template_name 		= 'registration/um1_signup.html'
	slug_field 			= 'slug'
	slug_url_kwargs 	= 'slug'
	success_url 		= reverse_lazy('accounts:profile')



class UpdateUm1View(UpdateView):
	model 				= CustomUserModel
	um1_model 			= UserModel1
	form_class 			= CustomeUserUpdateForm
	um1_form_class 		= UM1ChangeForm
	slug_field 			= 'slug'
	slug_url_kwargs 	= 'slug'
	template_name 		= 'accounts/um1_update.html'


	def get_object(self, queryset=None):
		cum_obj 		= self.model.objects.get(slug=self.kwargs.get('slug'))
		return cum_obj


	def post(self, request, *args, **kwargs):
		# getting objects of models
		cum_id 			= self.get_object().u_id
		um1_obj 		= self.um1_model.objects.filter(user_id=cum_id).first()

		# getting forms
		cum_form 		= self.form_class(request.POST, instance=self.get_object())
		um1_form 		= self.um1_form_class(request.POST, instance=um1_obj)

		#process forms
		if cum_form.is_valid() and um1_form.is_valid():
			cum_form 	= cum_form.save(commit=False)
			cum_form.save()
			um1_form 	= um1_form.save(commit=False)
			um1_form.save()
			
			return HttpResponseRedirect(reverse_lazy('accounts:profile'))
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