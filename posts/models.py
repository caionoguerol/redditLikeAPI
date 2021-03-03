from django.db import models
from helpers.models import FieldsModel, TimestampModel
from topics.models import Topic


# Create your models here.


class Post(FieldsModel, TimestampModel):
    content = models.TextField()
    url_name = models.SlugField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)



