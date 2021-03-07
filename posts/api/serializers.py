from rest_framework import serializers

from comments.api.serializers import CommentSerializer
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)

    class Meta:
        
        model = Post
        fields = ('id', 'title', 'content', 'comment_set', 'created_at', 'updated_at', 'topic', 'author')
        extra_kwargs = {'author': {'read_only': True}, 'topic': {'read_only': True}}

    def update(self, instance, validated_data):
        # raise_errors_on_nested_writes('update', self, validated_data)
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.save()

        return instance
