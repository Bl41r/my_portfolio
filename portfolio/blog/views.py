from django.views.generic import TemplateView
from .models import BlogArticle


class HomePageView(TemplateView):
    """Home View inheriting from TemplateView."""

    template_name = 'blog/index.html'
    model = BlogArticle

    def get_context_data(self):
        """View for the home page."""
        articles = BlogArticle.objects.filter(published=True).order_by('-date_published')
        context = {
            'page_title': 'Home',
        }
        return {'context': context, 'articles': articles}
