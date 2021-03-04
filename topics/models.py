from django.db import models
from helpers.models import FieldsModel, TimestampModel
from django.template.defaultfilters import slugify

# Create your models here.


class Topic(TimestampModel, FieldsModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    url_name = models.SlugField(max_length=50)

    def save(self, *args, **kwargs):
        self.url_name = slugify(self.name)
        super(Topic, self).save(*args, **kwargs)