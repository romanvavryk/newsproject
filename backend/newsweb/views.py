from django.shortcuts import render
import requests
import json
# Create your views here.

def home(request): 

	news_api_request = requests.get(
		"http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=e9eaf8af111a4b98b2015e8983233b1f"
	)
	api = json.loads(news_api_request.content)
	
	return render(request, 'home.html', {'api' : api})