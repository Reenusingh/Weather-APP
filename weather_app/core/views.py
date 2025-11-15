from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    weather_data = None
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = os.getenv('WEATHER_API_KEY')
        url =f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(url) # requests for Fetching data from API

        if response.status_code == 200:
            response = response.json()
            weather_data = {
                'city':response['name'],
                'temp': response['main']['temp'],
                'humidity': response['main']['humidity'],
                'wind_speed': response['wind']['speed'],
                'description':response['weather'][0]['description'].title(),
            }
        else:
            weather_data ={'error': 'City not found or API request failed.'}

    return render(request, 'core/index.html',{'weather_data':weather_data})
