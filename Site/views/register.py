from	django.urls						import	reverse_lazy
from	django.http.response			import	HttpResponse
from	django.contrib					import	messages
from	django.contrib.auth				import	login
from	django.views.generic			import	FormView
from	Site.models.myuser				import	MyUser
from	Site.forms						import	UserCreationForm

class	Register(FormView):
		template_name	= 'Site/view/register.html'
		success_url		= reverse_lazy('Site:main')
		form_class		= UserCreationForm
		
		def	form_valid(self, form: UserCreationForm) -> HttpResponse:
			_usr = form.save()
			login(self.request, _usr)
			messages.success(self.request, "✅ Registration success ✅")
			return	super().form_valid(form)
		
		def	form_invalid(self, form: UserCreationForm) -> HttpResponse:
			messages.success(self.request, "⚠️ Registration failed ⚠️")
			return	super().form_invalid(form)
