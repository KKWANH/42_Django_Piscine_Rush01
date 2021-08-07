from 	django							import forms
from 	django.db						import models


class	MyUser(models.Model):

		id				= models.EmailField(primary_key=True)
		password		= models.CharField(min_length=8, max_length=20, widget=forms.PasswordInput)
		nickName		= models.CharField(max_length=25, null=False)
		firstName		= models.CharField(null=False)
		lastName		= models.CharField(null=False)
		description		= models.TextField(max_length=420, null=False)
		profileImage	= models.ImageField()
