from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class AnoPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)#set's the time the post was posted
    author = models.ForeignKey(User, on_delete=models.CASCADE)#ON DELETE meaning if a user is deleted so does the posts of the user
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('anonymous')

class AnoComments(models.Model):
    from .models import AnoPost
    title= models.ForeignKey(AnoPost, on_delete= models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('anonycomments', kwargs={"pk" : self.pk})
