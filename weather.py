import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    main: str
    description: str
    icon: str
    temperature: int

def get_lat_lng(city_name, state_code, country_code, API_key):
    resp = requests.get(f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_key}').json()
    data = resp[0]
    lat, lng = data.get('lat'), data.get('lon')
    return lat, lng

def get_current_weather(lat, lng, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={API_key}&units=imperial').json()
    data = WeatherData(
        main=resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=int(resp.get('main').get('temp'))
    )
    return data

def main(city_name, state_name, country_name):
    lat, lng = get_lat_lng(city_name, state_name, country_name, api_key)
    weather_data = get_current_weather(lat, lng, api_key)
    return weather_data

if __name__ == "__main__":
    lat, lng = get_lat_lng('Minneapolis', 'MN', 'US', api_key)
    print(get_current_weather(lat, lng, api_key))