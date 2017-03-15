from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from aboutme.models import Profile


# Create your models here.
@python_2_unicode_compatible
class BlogArticle(models.Model):
    """The BlogArticle class."""

    title = models.CharField(max_length=128)
    text = models.TextField()
    date_published = models.DateField(auto_now_add=True, null=False)
    author = models.ForeignKey(Profile, related_name='articles')
    published = models.BooleanField(default=False)

    def __str__(self):
        """Make it show up recognizably in the shell/admin view."""
        return self.title
