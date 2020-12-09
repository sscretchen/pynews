from django.shortcuts import render, redirect

def index(request):
    """Main view of site"""

    context = {
    }
    return render(request, 'news/index.html', context)


def about(request):
    """Overview page of site"""
    return render(request, 'news/about.html')


def post_detail(request):
    """Single page view of API posts NOT scraped data"""
    return render(request, 'news/post_detail.html')
