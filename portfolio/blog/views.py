from django.views.generic import TemplateView
from .models import BlogArticle


class HomePageView(TemplateView):
    """Home View inheriting from TemplateView."""

    template_name = 'blog/index.html'
    model = BlogArticle

    def get_context_data(self, **kwargs):
        """View for the home page."""
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['page_title'] = 'Home'
        context['articles'] = BlogArticle.objects.filter(published=True).order_by('-date_published')
        return context
