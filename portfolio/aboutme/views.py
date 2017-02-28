from .models import Job, Education, Profile
from django.views.generic import TemplateView


# Create your views here.
class AboutMeView(TemplateView):
    """About me view."""

    template_name = 'aboutme/about-me.html'
    # model =

    def get_context_data(self, **kwargs):
        """View for the home page."""
        context = super(AboutMeView, self).get_context_data(**kwargs)
        context['page_title'] = 'About Me'
        context['jobs'] = Job.objects.all().order_by('-end_date')
        context['education'] = Education.objects.all().order_by('-graduation_date')
        context['profile'] = Profile.objects.filter(user__username='david').first()
        return context
