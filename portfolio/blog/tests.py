from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse_lazy
import factory
from blog.models import BlogArticle


# Create your tests here.
class BlogArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogArticle
    title = factory.Sequence(lambda n: "Article {}".format(n))
    text = 'blah blah blah'
    date_published = timezone.now()
    published = True


class BlogArticleTestCase(TestCase):
    """BlogArticle test class."""

    def setUp(self):
        """Set up the test."""
        self.articles = [BlogArticleFactory.create() for i in range(20)]
        self.authenticated_user = User(username='authenticated_user1')

    def test_blog_title(self):
        """Assert that the blog contains a title."""
        self.assertTrue("Article" in BlogArticle.objects.first().title)

    def test_article_has_no_author(self):
        """Assert the article has no author."""
        article = BlogArticle.objects.first()
        self.assertFalse(article.author)

    def test_article_has_author(self):
        """Assert the article has an author."""
        article = BlogArticle.objects.first()
        article.author = self.authenticated_user
        self.assertTrue(article.author)
