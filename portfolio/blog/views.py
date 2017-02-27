from django.shortcuts import render


# Create your views here.
def home_view(request):
    """The home view (blog)."""
    context = {
        'page_title': 'Home',
    }
    return render(request, 'blog/index.html', context)
