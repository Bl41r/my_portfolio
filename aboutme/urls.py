from django.conf.urls import url
from .views import AboutMeView

urlpatterns = [
    url(r'^$', AboutMeView.as_view(), name='aboutme_view'),
]
