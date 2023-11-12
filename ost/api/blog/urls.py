from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('article-create/', views.ArticleCreateView.as_view(), name='article-create'),
    path('articles/', views.ArticleDetailView.as_view()),
    path('comment-create/', views.CommentCreateView.as_view()),
    path('comments/<int:article_pk>', views.CommentShowView.as_view()),
]
