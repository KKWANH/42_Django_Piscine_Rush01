from django.views.generic import FormView
from Site.forms import ProfileForm
from Site.models import MyUser, Message
from django.urls import reverse_lazy

class ProfileView(FormView):
	form_class = ProfileForm
	template_name = 'Site/view/profile.html'

	def get_initial(self):
		initial = super().get_initial()
		myUser = MyUser.objects.get(nickName=str(self.kwargs.get('pk')))
		if myUser is not None:
			initial.update({'myEmail': myUser.email, 'description': myUser.description, \
				'firstName': myUser.firstName, 'lastName': myUser.lastName, 'profileImage': myUser.profileImage})
			if myUser.is_admin:
				initial['myAdmin'] = "Y"
			else:
				initial['myAdmin'] = "N"
		return initial

	def get_success_url(self):
		success_url = reverse_lazy('Site:profile', args=[str(self.kwargs.get('pk'))])
		return success_url

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		myUser = MyUser.objects.get(nickName=str(self.kwargs.get('pk')))
		print(self.request.user.is_superuser)
		if (not myUser.is_superuser) and (self.request.user.is_superuser):
			context['admin'] = True
		else:
			context['admin'] = False
		if self.request.user and self.request.user.is_authenticated and self.request.user.nickName == str(self.kwargs.get('pk')):
			context['owner'] = True
			context['start'] = False
		else:
			context['owner'] = False
			messages = Message.objects.filter(sender=self.request.user, receiver=myUser)
			messages |= Message.objects.filter(sender=myUser, receiver=self.request.user)
			if messages:
				context['start'] = False
			else:
				context['start'] = True
		return context

	def form_valid(self, form):
		myUser = MyUser.objects.get(nickName=str(self.kwargs.get('pk')))
		try:
			oldEmail = myUser.email
			newEmail = form.cleaned_data['myEmail']
			if oldEmail == newEmail:
				raise MyUser.DoesNotExist
			if oldEmail != newEmail and MyUser.objects.get(email=newEmail):
				raise AttributeError
		except AttributeError:
			form._errors['myEmail'] = form.error_class([u'Existing Email'])
			return super().form_invalid(form)
		except MyUser.DoesNotExist:
			myUser.email = form.cleaned_data['myEmail']
			myUser.firstName = form.cleaned_data['firstName']
			myUser.lastName = form.cleaned_data['lastName']
			myUser.profileImage = form.cleaned_data['profileImage']
			myUser.description = form.cleaned_data['description']
			if form.cleaned_data['myAdmin'] and form.cleaned_data['myAdmin'] == 'Y':
				myUser.is_admin = True
			else:
				myUser.is_admin = False
			myUser.save()
			return super().form_valid(form)
		except Exception:
			return super().form_invalid(form)
		return super().form_invalid(form)

	def form_invalid(self, form):
		print(form._errors)
		return super().form_invalid(form)


