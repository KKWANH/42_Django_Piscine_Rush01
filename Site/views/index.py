from	django.contrib.auth.mixins		import	LoginRequiredMixin
from	django.views.generic			import	ListView
from	django.urls.base				import	reverse_lazy
from	django.shortcuts				import	render
from	Site.models.post				import	PostModel

# class	Index(LoginRequiredMixin, ListView):
# 		login_url		= reverse_lazy('Site:login')
# 		paginate_by		= 10
# 		template_name	= 'intranet/pages/main/main.html'