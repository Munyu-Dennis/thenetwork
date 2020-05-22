from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)#set's the time the post was posted
    author = models.ForeignKey(User, on_delete=models.CASCADE)#ON DELETE meaning if a user is deleted so does the posts of the user
    def __str__(self):
        return self.title
    def get_pk(self):
        p_k = {"pk" : self.pk}
        return p_k
    def get_absolute_url(self):
        p_k = self.get_pk()
        return reverse('post-detail', kwargs=p_k)



class Comments(models.Model):
    from .models import Post
    title= models.ForeignKey(Post, on_delete= models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)#set's the time the post was posted
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def get_absolute_url(self):
        p_k = Post.get_pk(self)
        return reverse('comments', kwargs=p_k)