from rest_framework import serializers
from topics.models import Topic


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'title', 'name', 'description', 'url_name', 'created_at', 'updated_at', 'author')
        extra_kwargs = {'author': {'read_only': True},'url_name': {'read_only': True}}

    # def create(self, validated_data):
    #     topic = Topic(title=validated_data['title'], name=validated_data['name'],
    #                   description=validated_data['description'], url_name=validated_data['url_name'],
    #                   author=validated_data['user_profile'])
    #     topic.save()
    #
    #     return topic
