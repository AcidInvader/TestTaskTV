from django.contrib.auth import get_user_model
from rest_framework import serializers
from blog.models import Article, Comment


User = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username']


class ArticleCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'title', 'content']


class ArticleDetailSerializer(ArticleCreateSerializer):

    class Meta(ArticleCreateSerializer.Meta):
        fields = ArticleCreateSerializer.Meta.fields


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'article']

        def create(self, validated_data):
            user = self.context['request'].user
            validated_data['user'] = user
            return super().create(validated_data)


class CommentShowSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'article']


















