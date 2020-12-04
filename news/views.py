from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import json

def index(request):
    """Main view of site"""

    # Pulling Coding news from https://developer-tech.com/
    code_data = requests.get("https://developer-tech.com/news/2020/")
    code_soup = BeautifulSoup(code_data.content, 'html.parser')
    code_headings = code_soup.find_all("h3")
    code_headings = code_headings[0:3]
    code_news = []

    for code_article in code_headings:
        code_news.append(code_article.text)

    # Pulling Gaming news from https://developer-tech.com/
    game_data = requests.get("https://www.gamespot.com/games/")
    game_soup = BeautifulSoup(game_data.content, 'html.parser')
    game_headings = game_soup.find_all("h4")
    game_headings = game_headings[1:4]
    game_news = []

    for game_article in game_headings:
        game_news.append(game_article.text)

    context = {
        'code_news': code_news,
        'game_news': game_news,
    }
    return render(request, 'news/index.html', context)


def about(request):
    """Overview page of site"""
    return render(request, 'news/about.html')


def post_detail(request):
    """Single page view of API posts NOT scraped data"""
    return render(request, 'news/post_detail.html')
