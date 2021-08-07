from 	django.db						import models
from 	django.contrib.auth.models 		import User
from 	django.db.models.deletion 		import CASCADE
class	MyUser(models.Model):
		user			= models.OneToOneField(User, on_delete=CASCADE, related_name="myUser")
		nickName		= models.CharField(primary_key=True, max_length=25, null=False)
		email			= models.EmailField(unique=True)
		firstName		= models.CharField(max_length=25, null=False)
		lastName		= models.CharField(max_length=25, null=False)
		description		= models.TextField(max_length=420, null=False)
		profileImage	= models.ImageField()
