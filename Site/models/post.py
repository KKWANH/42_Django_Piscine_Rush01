from 	django.db						import models
from 	Site.models				 		import MyUser
from 	django.db.models.deletion 		import CASCADE


class	Comment(models.Model):
		id			= models.AutoField(primary_key=True)
		userID		= models.ForeignKey(MyUser, on_delete=CASCADE, related_name="post")
		title		= models.CharField(max_length=32)
		content		= models.TextField()
		created		= models.DateTimeField(auto_now_add=True)
