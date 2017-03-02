from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from aboutme.models import Profile


# Create your models here.
@python_2_unicode_compatible
class Project(models.Model):
    """The Project class."""

    title = models.CharField(max_length=128)
    text = models.TextField()
    github_url = models.URLField()
    date_added = models.DateField(auto_now_add=True, null=False)
    author = models.ForeignKey(Profile, related_name='projects')

    def __str__(self):
        """Make it show up recognizably in the shell/admin view."""
        return self.title
