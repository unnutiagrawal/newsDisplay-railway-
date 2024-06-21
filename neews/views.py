from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup

def home(request):
    return render(request, 'index2.html')

def fetch_indian_railway_news(request):
    url = "https://news.google.com/rss/search?q=indian+railway"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')
    news = [{'title': item.title.text, 'link': item.link.text} for item in items]
    return JsonResponse(news, safe=False)

def fetch_global_railway_news(request):
    url = "https://news.google.com/rss/search?q=global+railway"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    items = soup.find_all('item')
    news = [{'title': item.title.text, 'link': item.link.text} for item in items]
    return JsonResponse(news, safe=False)
