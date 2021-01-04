from django.shortcuts import render
from newsapi import NewsApiClient


 
# Create your views here.
def index(request):
    import json
    import requests
    
    news_api_request=requests.get("http://newsapi.org/v2/top-headlines?country=in&category=technology&apiKey=f0c7e94b68ba40619dd2fb2bbb988101")
    api=json.loads(news_api_request.content)
    return render(request,'news/index.html',{'api':api})