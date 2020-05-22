from django.contrib import admin
from .models import Post, Comments
admin.site.register(Post)#help the admin to do changes of Posts
admin.site.register(Comments)
