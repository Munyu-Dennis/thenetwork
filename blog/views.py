from django.shortcuts import render, get_object_or_404
from .models import Post, Comments
from django.views.generic import ( 
            ListView, 
            DetailView,
            CreateView,
            UpdateView,
            DeleteView
            
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
'''
def home(request):
    context = {
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html', context)
'''
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'#<app>/<model>_<view_type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'#<app>/<model>_<view_type>.html
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post
  


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post 
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class CommentsListView(ListView):
    template_name = 'blog/commments_list.html'#<app>/<model>_<view_type>.html
    context_object_name = 'comments'
    queryset = Comments.objects.all()
    ordering = ['-date_posted']
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super(CommentsListView, self).get_context_data(**kwargs)
        context["posts"] = Post.objects.all() 
        #context["pos"] = [Post.objects.all(), Comments.objects.all()]
        context["comments"] = Comments.objects.all()
        return context
class CommentDetailView(DetailView):
    model = Comments
    template_name = 'blog/comment_detail.html'

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comments
    fields = [ 'title', 'content']
    template_name = 'blog/comments_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comments
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comments
    success_url = '/'
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

'''
def comments(request):
    context={
        'comments': Comment.objects.all(),
        'post':Post.objects.all()
    }
    return render(request, 'blog/comments.html', context)'''
def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
