from django.urls import path, include
# from .views import ArticleCreateView, ArticleDetailView
from . import views


urlpatterns = [
    path('article-create/', views.ArticleCreateView.as_view()),
    path('articles/', views.ArticleDetailView.as_view()),
    path('comment-create/', views.CommentCreateView.as_view()),
    path('comments/<int:article_pk>', views.CommentShowView.as_view()),
]