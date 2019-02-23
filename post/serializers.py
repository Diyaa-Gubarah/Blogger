from rest_framework import serializers

from .models import Comment, Like, Post


class PostSerializer(serializers.ModelSerializer):
    like = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = ('pk','user', 'group', 'title', 'content', 'created_at', 'like',)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk','post', 'comment_auther',
                  'comment_text', 'comment_create_date',)
        depth = 1


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('pk','post','user','num_of_like')
