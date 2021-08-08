from	django.urls						import	path
from	.								import	views
from 	django.conf 					import settings
from 	django.conf.urls.static 		import static

urlpatterns = [
	path('',					views.Index.as_view(),			name='index'),
	# path('login/',				views.Login.as_view(),			name='login'),
	# path('logout/',				views.Logout.as_view(),			name='logout'),
	# path('register/',			views.Register.as_view(),		name='register'),
	# path('post/',				views.Post.as_view(),			name='post'),
	# path('login',				views.Index.as_view(),			name='login'),
	# path('test/', views.TestView.as_view(), name="test"),
	# path('profile/<str:pk>/',	views.ProfileView.as_view(),	name='profile'),
	# path('discussions/',	views.DiscussionListView.as_view(),	name='discussionList'),
	# path('discussions/<str:user1>&<str:user2>/',	views.DiscussionDetailView.as_view(),	name='discussionDetail'),
] + static(settings.MEDIA_URL,	document_root=settings.MEDIA_ROOT)
