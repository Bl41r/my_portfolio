from rest_framework import serializers
from projects.models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'github_url', 'text', 'date_added', 'author')
