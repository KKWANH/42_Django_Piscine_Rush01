from	django.urls						import	path
from	.								import	views

urlpatterns = [
	path('',					views.Index.as_view(),			name='index'),
	# path('login/',				views.Login.as_view(),			name='login'),
	# path('logout/',				views.Logout.as_view(),			name='logout'),
	# path('register/',			views.Register.as_view(),		name='register'),
	# path('post/',				views.Post.as_view(),			name='post'),
	# path('login',				views.Index.as_view(),			name='login'),
]
