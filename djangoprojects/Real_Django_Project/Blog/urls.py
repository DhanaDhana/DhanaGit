from django.urls import path
from .views import (
    PostListView,
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostUpdateView,
    UserPostListView
)
from . import views


urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),

    path('post/<int:pk>',PostDetailView.as_view(),name="post-detail"),

    path('post/new/',PostCreateView.as_view(),name='post-create'),

    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update'),

    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete'),
    path('user/<str:username>/',UserPostListView.as_view(),name='user-posts'),
    path('latest_posts',views.LatestListView,name='latest_posts'),
    path('top_questions',views.top_questions,name='top_questions'),
    path('about/',views.about,name='blog-about'),
]