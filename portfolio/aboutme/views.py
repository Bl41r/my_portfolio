from .models import Job, Education, Profile
from django.views.generic import TemplateView


# Create your views here.
class AboutMeView(TemplateView):
    """About me view."""

    template_name = 'aboutme/about-me.html'

    def get_context_data(self, **kwargs):
        """View for the home page."""
        context = super(AboutMeView, self).get_context_data(**kwargs)
        context['page_title'] = 'About Me'
        context['jobs'] = Job.objects.filter(profile__user__username='david').all()
        context['profile'] = Profile.objects.filter(user__username='david').first()
        context['education'] = Education.objects.filter(profile__user__username='david').all()
        return context
