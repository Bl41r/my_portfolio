from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from projects.models import Project


# Create your models here -- jobs, education, profile
@python_2_unicode_compatible
class Job(models.Model):
    """The Job class."""

    title = models.CharField(max_length=128)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    skills = TaggableManager()

    def __str__(self):
        """Str representation of model."""
        return self.title


@python_2_unicode_compatible
class Education(models.Model):
    """The education class."""

    school = models.CharField(max_length=128)
    degree = models.CharField(max_length=128)
    graduation_date = models.DateField()

    def __str__(self):
        return self.school + ' ' + self.degree


@python_2_unicode_compatible
class Profile(models.Model):
    """The user profile."""

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    bio = models.TextField(default="")
    educations = models.ForeignKey(Education, null=True, related_name='profile', on_delete=models.CASCADE)
    jobs = models.ForeignKey(Job, null=True, related_name='profile', on_delete=models.CASCADE)
    projects = models.ForeignKey(Project, null=True, related_name='profile', on_delete=models.CASCADE)

    @property
    def is_active(self):
        return self.user.is_active

    def __str__(self):
        fn = self.user.get_full_name().strip() or self.user.get_username()
        return "{}".format(fn)


@receiver(post_save, sender=User)
def make_user_profile(sender, instance, **kwargs):
    """Make a new user profile associated with new user."""
    if kwargs["created"]:
        Profile(user=instance).save()
