from django.db import models
from pages.models import Profile


class Chat(models.Model):
    def __str__(self):
        return f'{self.id}'


class Message(models.Model):
    content = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(Profile, related_name='from_profile', on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, related_name='get_msg', on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ['date']


class Chat_members(models.Model):
    chat = models.ForeignKey(Chat, related_name='members', on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, related_name='chats', on_delete=models.CASCADE)
    last_viewed = models.DateTimeField(blank=True, null=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f'chat id: {self.chat} user:{self.profile.user} last_viewed:{self.last_viewed} deleted:{self.deleted}'

