from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('article-create/', views.ArticleCreateView.as_view(), name='article-create'),
    path('article-delete/<int:pk>/', views.ArticleDeleteView.as_view(), name='article-delete'),
    path('articles/', views.ArticleDetailView.as_view(), name='article-list'),
    path('comment-create/', views.CommentCreateView.as_view(), name='comment-create'),
    path('comments/', views.CommentShowView.as_view(), name='comments-list'),
]
