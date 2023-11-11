from rest_framework.generics import CreateAPIView, ListAPIView
from blog.models import Article, Comment
from django.db.models import QuerySet

from . import serializers


class ArticleCreateView(CreateAPIView):
    permission_classes = ()
    serializer_class = serializers.ArticleCreateSerializer


class ArticleDetailView(ListAPIView):
    permission_classes = ()
    serializer_class = serializers.ArticleDetailSerializer

    def get_queryset(self) -> QuerySet[Article]:
        return Article.objects.all()


class CommentCreateView(CreateAPIView):
    permission_classes = ()
    serializer_class = serializers.CommentCreateSerializer


class CommentShowView(ListAPIView):
    permission_classes = ()
    serializer_class = serializers.CommentShowSerializer

    def get_queryset(self):
        article_id = self.kwargs['article_pk']
        return Comment.object.filter(article_id=article_id)








