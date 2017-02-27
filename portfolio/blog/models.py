from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings


# Create your models here.
@python_2_unicode_compatible
class BlogArticle(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True, null=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)
    published = models.BooleanField(default=False)
