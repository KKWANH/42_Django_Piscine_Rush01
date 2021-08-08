from 	django.db						import models
from 	django.db.models.deletion 		import CASCADE
from 	Site.models.myuser		 		import MyUser


class	Post(models.Model):

		id			= models.AutoField(primary_key=True)
		userID		= models.ForeignKey(MyUser, on_delete=CASCADE, related_name="post")
		title		= models.CharField(max_length=40)
		content		= models.TextField()
		created		= models.DateTimeField(auto_now_add=True)
