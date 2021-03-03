from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'url_name', 'created_at', 'updated_at', 'topic', 'author')
        extra_kwargs = {'author': {'read_only': True}}

    def update(self, instance, validated_data):
        # raise_errors_on_nested_writes('update', self, validated_data)
        instance.title = validated_data['title']
        instance.content = validated_data['content']
        instance.url_name = validated_data['url_name']
        instance.save()

        return instance
