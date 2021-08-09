from 	django.db						import	models
from 	django.db.models.deletion 		import	CASCADE
from 	Site.models.myuser				import	MyUser
from	Site.models.post				import	Post


class	Comment(models.Model):
		id			= models.AutoField(primary_key=True)
		postID		= models.ForeignKey(Post, on_delete=CASCADE, related_name="comment")
		userID		= models.ForeignKey(MyUser, on_delete=CASCADE, related_name="comment")
		commentID	= models.ForeignKey('self', on_delete=CASCADE, related_name="recomment", null=True)
		content		= models.TextField(max_length=500, null=False)
		created		= models.DateTimeField(auto_now_add=True, null=False)
		updated		= models.DateTimeField(auto_now=True, null=False)
		is_active	= models.BooleanField(default=True)