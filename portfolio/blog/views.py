from django.views.generic import TemplateView
from .models import BlogArticle


class HomePageView(TemplateView):
    """Return the Home View inheriting from TemplateView."""

    template_name = 'blog/index.html'
    model = BlogArticle

    def get_context_data(self):
        """View for the home page."""
        articles = BlogArticle.objects.all()
        context = {
            'page_title': 'Home',
        }
        return {'context': context, 'articles': articles}
