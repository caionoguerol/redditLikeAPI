from django.db import models
from helpers.models import FieldsModel, TimestampModel
from posts.models import Post


# Create your models here.


class Comment(FieldsModel, TimestampModel):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)