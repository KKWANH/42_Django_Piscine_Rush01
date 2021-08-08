from django.views.generic import ListView
from django.shortcuts import redirect, render
from Site.models import MyUser, Message
from django.urls import reverse_lazy

class DiscussionListView(ListView):
	paginate_by = 10
	model = Message
	template_name = 'Site/view/discussion_list.html'

	def get_queryset(self):
		myUser = MyUser.objects.get(nickName=self.request.user.nickName)
		messages = Message.objects.filter(sender=myUser, last=True)
		messages |= Message.objects.filter(receiver=myUser, last=True)
		if messages:
			messages = messages.order_by('-created')
		return messages

class DiscussionDetailView(ListView):
	model = Message
	fields = ['content']
	template_name = 'Site/view/discussion_detail.html'

	def get_queryset(self):
		user1 = MyUser.objects.get(nickName=str(self.kwargs.get('user1')))
		user2 = MyUser.objects.get(nickName=str(self.kwargs.get('user2')))
		messages = Message.objects.filter(sender=user1, receiver=user2)
		messages |= Message.objects.filter(sender=user2, receiver=user1)
		return messages.order_by('created')

	def post(self, request, user1, user2):
		if request.POST.get('content'):
			sender = MyUser.objects.get(nickName=user1)
			receiver = MyUser.objects.get(nickName=user2)
			try:
				oldLast = Message.objects.get(sender=sender, receiver=receiver, last=True)
				oldLast.last = False
				oldLast.save()
			except Message.DoesNotExist:
				try:
					oldLast = Message.objects.get(sender=receiver, receiver=sender, last=True)
					oldLast.last = False
					oldLast.save()
				except Message.DoesNotExist:
					pass
			finally:
				new = Message(
					sender=sender,
					receiver=receiver,
					content=request.POST.get('content')
				)
				new.save()
			return redirect(reverse_lazy('Site:discussionDetail', kwargs={'user1': user1, 'user2': user2}))
		else:
			return redirect(reverse_lazy('Site:discussionDetail', kwargs={'user1': user1, 'user2': user2}))
