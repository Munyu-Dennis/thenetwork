from django.urls import path
from . import views#. --> from here
from .views import (
    AnoPostListView, 
    AnoPostDetailView,
    AnoPostCreateView,
    AnoPostUpdateView,
    AnoPostDeleteView,
    #UserPostListView,#<--WORKON THIS LATER
    AnoCommentsListView,
    AnoCommentCreateView,
    AnoCommentDetailView,
    AnoCommentUpdateView,
    AnoCommentDeleteView

)
urlpatterns = [
    path('', AnoPostListView.as_view(), name='anonymous'),
    path('user/info', views.whatis , name='user-info'),
    path('anonypost/<int:pk>/', AnoPostDetailView.as_view(), name='anonypost-detail'),
    path('anonymous/anonypost/new/', AnoPostCreateView.as_view(), name='anonypost-create'),
    path('anonymous/anonypost/<int:pk>/update', AnoPostUpdateView.as_view(), name='anonypost-update'),
    path('anonymous/anonypost/<int:pk>/delete', AnoPostDeleteView.as_view(), name='anonypost-delete'),
    

]
#comment urls 
urlpatterns += [
    path('anonypost/<int:pk>/anonycomments', AnoCommentsListView.as_view(), name='anonycomments'), 
    path('anonypost/<int:pk>/anonycomment', AnoCommentCreateView.as_view(), name='anonycomment-create'),
    path('anonycomment/<int:pk>/', AnoCommentDetailView.as_view(), name='anonycomment-detail'),
    path('anonycomment/<int:pk>/update', AnoCommentUpdateView.as_view(), name='anonycomment-update'),
    path('anonycomment/<int:pk>/delete', AnoCommentDeleteView.as_view(), name='anonycomment-delete')
    ]
