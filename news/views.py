from django.shortcuts import render
import requests
import json

def index(request):
    """Main view of site"""
    tech_api_request = requests.get("http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=e8c53fe0ff3d44da82a8efc233d8247d")
    api = json.loads(tech_api_request.content)

    context = {
        'api': api,
    }
    return render(request, 'news/index.html', context)


def about(request):
    """Overview page of site"""
    return render(request, 'news/about.html')


def post_detail(request):
    """Single page view of each post"""
    return render(request, 'news/post_detail.html')
