from rest_framework import serializers

from posts.api.serializers import PostSerializer
from topics.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    post_set = PostSerializer(many=True, read_only=True)

    class Meta:

        model = Topic
        fields = ('id', 'title', 'name', 'description', 'post_set', 'url_name', 'created_at', 'updated_at', 'author')
        lookup_field = 'url_name'
        extra_kwargs = {'author': {'read_only': True}, 'url_name': {'read_only': True}}


