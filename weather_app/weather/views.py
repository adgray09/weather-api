from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=94ec941f238c8071ffbbda04f44bf3ac'
    city = 'San Francisco'
    
    r = requests.get(url.format(city)).json()
    
    city_weather = {
        'city': city,
        'weather': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }
    
    context = {'city_weather': city_weather}
     
    return render(request, 'weather/weather.html', context)