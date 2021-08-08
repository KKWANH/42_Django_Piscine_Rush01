from	django.urls						import	path
from	.								import	views
from 	django.conf 					import settings
from 	django.conf.urls.static 		import static

urlpatterns = [
	path('test/', views.TestView.as_view(), name="test"),
	path('profile/<str:pk>/',	views.ProfileView.as_view(),	name='profile'),
	path('discussions/',	views.DiscussionListView.as_view(),	name='discussionList'),
	path('discussions/<str:user1>&<str:user2>/',	views.DiscussionDetailView.as_view(),	name='discussionDetail'),
] + static(settings.MEDIA_URL,	document_root=settings.MEDIA_ROOT)
