from django.shortcuts import render, get_object_or_404
from .models import AnoPost, AnoComments
from django.views.generic import ( 
            ListView, 
            DetailView,
            CreateView,
            UpdateView,
            DeleteView
            
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
class AnoPostListView(ListView):
    model = AnoPost
    template_name = 'anonymous/anonymous.html'#<app>/<model>_<view_type>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5
    


class AnoPostDetailView(DetailView):
    model = AnoPost
    template_name = 'anonymous/anopost_detail.html'


class AnoPostCreateView(LoginRequiredMixin, CreateView):
    model = AnoPost
    template_name = 'anonymous/anopost_form.html'
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class AnoPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AnoPost
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class AnoPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AnoPost 
    success_url = '/anonymous'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
class AnoCommentsListView(ListView):
    model = AnoComments 
    template_name = 'anonymous/anocommments_list.html'#<app>/<model>_<view_type>.html
    context_object_name = 'comments'
    ordering = ['-date_posted']
    paginate_by = 5

class AnoCommentDetailView(DetailView):
    model = AnoComments
    template_name = 'anonymous/anocomment_detail.html'

class AnoCommentCreateView(LoginRequiredMixin, CreateView):
    model = AnoComments
    fields = [ 'title', 'content']
    template_name = 'anonymous/anocomments_form.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class AnoCommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = AnoComments
    fields = ['title', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False

class AnoCommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = AnoComments
    success_url = 'anonymous'
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.author:
            return True
        return False
def whatis(request):
    return render(request, 'anonymous/whatis.html')
