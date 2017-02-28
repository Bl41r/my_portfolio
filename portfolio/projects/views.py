"""Views for projects."""


from django.views.generic import TemplateView
from .models import Project


class ProjectView(TemplateView):
    """Return the Project View, inheriting from TemplateView."""

    template_name = 'projects/index.html'
    model = Project

    def get_context_data(self):
        """View for the home page."""
        projects = Project.objects.all().order_by('-date_added')
        context = {
            'page_title': 'Home',
        }
        return {'context': context, 'articles': projects}
