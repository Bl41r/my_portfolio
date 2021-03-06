from rest_framework import viewsets
from projects.models import Project
from api.serializers import ProjectSerializer
from rest_framework import permissions
from rest_framework.response import Response
from api.permissions import IsAuthorOrReadOnly


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    """The ViewSet for the project model."""

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthorOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        """Associate user with instance."""
        serializer.save(author=self.request.user.profile)
