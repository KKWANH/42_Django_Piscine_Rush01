from	typing							import	Any
from	django							import	http
from	django.http						import	request, HttpRequest
from	django.http.response			import	Http404, HttpResponse, HttpResponseBase
from	django.urls						import	reverse_lazy, reverse
from	django.http.response			import	HttpResponseBase
from	django.contrib					import	messages
from	django.contrib.auth.mixins		import	LoginRequiredMixin
from	django.shortcuts				import	redirect, render
from	django.views.generic			import	FormView, DetailView, RedirectView
from	Site.models.post				import	Post
from	Site.models.comment				import	Comment
from	Site.forms						import	PostForm


class	PostUserCheckMixin:
	def	dispatch(self, request: HttpRequest, post_id, *args: Any, **kwargs: Any) -> HttpResponse:
		try:
			post: Post = Post.objects.get(id=post_id)
		except Post.DoesNotExist:
			raise	Http404()
		if post.userID != request.user and not request.user.is_staff:
			messages.error(request, "⚠️ Permission denied ⚠️")
			return	redirect("Site:main")
		self.instance = post
		return	super().dispatch(request, post_id, *args, **kwargs)


class	PostView(LoginRequiredMixin, FormView):
		template_name	= 'Site/view/post_new.html'
		form_class		= PostForm
		login_url		= reverse_lazy('Site:login')

		def	get_success_url(self) -> str:
			print("here!!2")
			print(self.instance.id)
			return	reverse('Site:post-detail', args=[self.instance.id])
		
		def	form_valid(self, form: PostForm) -> HttpResponse:
			post:Post	= form.save(commit=False)
			post.userID = self.request.user
			print("here!!")
			print(post.userID)
			post.save()
			self.instance = post
			messages.success(self.request, "✅ Posting succeess ✅")
			return	super().form_valid(form)

		def	form_invalid(self, form: PostForm) -> HttpResponse:
			return	super().form_invalid(form)

class	PostDetailView(LoginRequiredMixin, DetailView):
		template_name	= 'Site/view/post_detail.html'
		login_url		= reverse_lazy('Site:login')
		model			= Post
		pk_url_kwarg	= 'post_id'

		def	get_context_data(self, **kwargs):
			_ctx		= super().get_context_data(**kwargs)
			_pst: Post	= _ctx['object']
			if _pst.is_active == False:
				raise	Http404()
			return	_ctx