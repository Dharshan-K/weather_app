from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
# Create your views here.

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=cfa61d60683559971201c73e09953d17'
	# city = 'Las Vegas'
	cities = City.objects.all()

	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()

	weather_data=[]

	form = CityForm()

	for city in cities:
		city_weather = requests.get(url.format(city)).json()
		weather = {
		'city':city,
		'temperature' : city_weather['main']['temp'],
		'description' : city_weather['weather'][0]['description'],
		'icon' : city_weather['weather'][0]['icon']
		}
		weather_data.append(weather)

	context = {'weather_data':weather_data}

	

	

	
	return render(request, "index.html", context)