from rest_framework import serializers
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Project
        fields = ('title', 'github_url', 'text', 'date_added', 'author')
