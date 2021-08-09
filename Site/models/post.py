from 	django.db						import models
from 	django.db.models.deletion 		import CASCADE
from 	Site.models.myuser		 		import MyUser


class	Post(models.Model):
		id			= models.AutoField(primary_key=True)
		userID		= models.ForeignKey(MyUser, on_delete=CASCADE, related_name="post")
		title		= models.CharField(max_length=40)
		content		= models.TextField(null=False)
		created		= models.DateTimeField(auto_now_add=True, null=False)
		updated		= models.DateTimeField(auto_now=True, null=False)
		is_active	= models.BooleanField(default=True, null=False)

		class	Meta:
				ordering = ('created',)
		
		def	__str__(self):
			return	self.title
