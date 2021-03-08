from rest_framework import serializers
from comments.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'post', 'author')
        extra_kwargs = {'author': {'read_only': True}, 'post': {'read_only': True}}

    def update(self, instance, validated_data):
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.save()

        return instance