from django.db import models
from Site.models import Post, MyUser
from django.db.models.deletion import CASCADE

class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	postID = models.ForeignKey(Post, on_delete=CASCADE, related_name="comment")
	userID = models.ForeignKey(MyUser, on_delete=CASCADE, related_name="comment")
	commentID = models.ForeignKey('self', on_delete=CASCADE, related_name="recomment", null=True)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)

