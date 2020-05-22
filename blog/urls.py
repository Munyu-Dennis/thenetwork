from django.urls import path
from . import views#. --> from here
from .views import (
    PostListView, 
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentsListView,
    CommentCreateView,
    CommentDetailView,
    CommentUpdateView,
    CommentDeleteView

)
urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about')

]
#comment urls 
urlpatterns += [
    path('post/<int:pk>/comments', CommentsListView.as_view(), name='comments'), 
    path('post/<int:pk>/comment', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('comment/<int:pk>/update', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='comment-delete')
    ]
