from django.shortcuts import render
from rest_framework import viewsets
from projects.models import Project
from api.serializers import ProjectSerializer
from api import permissions
from rest_framework.response import Response


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    """The ViewSet for the project model."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (permissions.IsOwnerOrReadOnly,)

    def list(self, request):
        serializer = ProjectSerializer(self.queryset, many=True)
        return Response(serializer.data)
