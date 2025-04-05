import requests
import os 

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather_data():
    params = {
        'q': city, 
        'appid': API_KEY, 
        'units': 'metric'

    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json 

        return {
            'city': data['name'], 
            'temperature': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
            'humidity':data['main']['speed'] 
        }
    
    except response.RequestException as e:
        return {'errpr': str(e)}
