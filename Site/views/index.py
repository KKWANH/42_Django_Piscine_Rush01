from	django.contrib.auth.mixins		import	LoginRequiredMixin
from	django.views.generic			import	ListView
from	django.urls.base				import	reverse_lazy
from	django.shortcuts				import	render
from	Site.models.post				import	Post

class	Index(LoginRequiredMixin, ListView):
		login_url		= reverse_lazy('Site:login')
		paginate_by		= 10
		template_name	= 'Site/pages/main/main.html'
		model			= Post
		queryset		= model.objects.order_by('-id')