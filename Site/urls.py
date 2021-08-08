from 	django.conf 					import settings
from 	django.conf.urls.static 		import static
from	django.urls						import	path
from	.								import	views

app_name = "Site"

urlpatterns = [
	path('',					views.Main.as_view(),					name='main'),
	path('login/',				views.Login.as_view(),					name='login'),
	path('logout/',				views.Logout.as_view(),					name='logout'),
	path('register/',			views.Register.as_view(),				name='register'),
	path('test/',				views.TestView.as_view(),				name="test"),
	path('profile/<str:pk>/',	views.ProfileView.as_view(),			name='profile'),
	path('discussions/',		views.DiscussionListView.as_view(), 	name='discussionList'),
	path('discussions/<str:user1>&<str:user2>/',
								views.DiscussionDetailView.as_view(),	name='discussionDetail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
