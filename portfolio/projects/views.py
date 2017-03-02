"""Views for projects."""


from django.views.generic import TemplateView
from .models import Project


class ProjectView(TemplateView):
    """Return the Project View, inheriting from TemplateView."""

    template_name = 'projects/projects.html'
    model = Project

    def get_context_data(self, **kwargs):
        """View for the home page."""
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(profile__user__username='david').all().order_by('-date_added')
        context['page_title'] = 'My Projects'
        return context
