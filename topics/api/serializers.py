from rest_framework import serializers
from topics.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id','title', 'name', 'description', 'url_name', 'created_at', 'updated_at', 'user_profile')
        extra_kwargs = {'user_profile': {'read_only': True}}
