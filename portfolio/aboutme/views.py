from .models import Job, Education, Profile
from django.views.generic import TemplateView


# Create your views here.
class AboutMeView(TemplateView):
    """About me view."""

    template_name = 'aboutme/about-me.html'
    # model =

    def get_context_data(self):
        """View for the home page."""
        jobs = Job.objects.all().order_by('-end_date')
        education = Education.objects.all().order_by('-graduation_date')
        # profile =
        context = {
            'page_title': 'About Me',
        }
        return {'context': context, 'jobs': jobs, 'education': education}
