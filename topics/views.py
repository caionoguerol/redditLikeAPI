from topics.models import Topic
from topics.api.serializers import TopicSerializer
from rest_framework import viewsets



class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()