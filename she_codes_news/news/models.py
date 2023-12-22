# Users Setup Step 16: add a relationship between stories and users

from django.db import models
from django.contrib.auth import get_user_model


class NewsStory(models.Model):
    image_url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.TextField()
