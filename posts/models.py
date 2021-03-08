from django.db import models
from helpers.models import FieldsModel, TimestampModel
from topics.models import Topic





class Post(FieldsModel, TimestampModel):
    content = models.TextField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)



