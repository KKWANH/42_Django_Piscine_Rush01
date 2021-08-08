from 	django.db						import	models
from 	django.db.models.deletion 		import	CASCADE
from 	Site.models.myuser				import	MyUser
class	Message(models.Model):

		id			= models.AutoField(primary_key=True)
		sender		= models.ForeignKey(MyUser, on_delete=CASCADE, related_name="messageSent")
		receiver	= models.ForeignKey(MyUser, on_delete=CASCADE, related_name="messageReceived")
		content		= models.TextField()
		created		= models.DateTimeField(auto_now_add=True)
		last		= models.BooleanField(default=True)
