"""Tests for the blog app."""

from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse_lazy
import factory
from blog.models import BlogArticle


# Create your tests here.
class BlogArticleFactory(factory.django.DjangoModelFactory):
    """BlogArticle factory."""

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

    def test_blog_text(self):
        """Assert the text is correct."""
        self.assertTrue(BlogArticle.objects.first().text == 'blah blah blah')

    def test_blog_has_date_published(self):
        """Assert there is a date_published on article."""
        self.assertTrue(BlogArticle.objects.first().date_published)

    def test_article_has_no_author(self):
        """Assert the article has no author."""
        self.assertFalse(BlogArticle.objects.first().author)

    def test_article_has_author(self):
        """Assert the article has an author."""
        article = BlogArticle.objects.first()
        article.author = self.authenticated_user
        self.assertTrue(article.author)

    def test_correct_number_of_articles(self):
        """Assert that there are 20 articles."""
        self.assertTrue(len(BlogArticle.objects.all()) == 20)

    def test_published(self):
        """Assert that the blog article is published."""
        self.assertTrue(BlogArticle.objects.first().published)
