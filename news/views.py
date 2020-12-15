from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from stories.models import Story
import requests
import json


def index(request):
    """Main view of site"""
    api_key = "e8c53fe0ff3d44da82a8efc233d8247d"
    page = request.GET.get('page', 1)
    search = request.GET.get('search', None)

    if search is None or search == "top":
        url = f"https://newsapi.org/v2/top-headlines?country=us&page={1}&apiKey={api_key}"
    else:
        url = f"https://newsapi.org/v2/everything?q={search}&sortBy=popularity&page={page}&apiKey={api_key}"

    r = requests.get(url=url)
    data = r.json()
    if data["status"] != "ok":
        return HttpResponse("<h2>Request Failed</h2>")
    # Pull the first 3 articles with [:3] at the end
    data = data["articles"][:5]
    context = {
        "success": True,
        "data": [],
        "search": search
    }

    for i in data:
        context["data"].append({
            "title": i["title"],
            "description": i["description"],
            "url": i["url"],
            "source": i["source"],
            "image": i["urlToImage"],
            "publishedat": i["publishedAt"]
        })

    return render(request, 'news/index.html', context=context)


def about(request):
    """Overview page of site"""
    return render(request, 'news/about.html')


def post_detail(request):
    """Single page view of API posts NOT scraped data"""
    return render(request, 'news/post_detail.html')
