from dotenv import load_dotenv;
from pprint import pprint;
import requests;
import os;
    

load_dotenv()

#le damos un valor default a city(city=Medellin, en caso de que el usuario no marque nada)

def get_current_weather(city='Kansas'):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    weather_data = requests.get(request_url).json()

    return weather_data

if __name__ == '__main__':
    print('\n ***GET CURRENT WEATHER CONDITION***')

    city = input('Please, add a city: ')

    #Revisa si el usuario ingreso espacios en blanco or nothing at all

    if not bool(city.strip()):
        city = "Toronto"

    weather_data = get_current_weather(city)

    if weather_data == {'cod': '404', 'message': 'city not found'}:
        weather_data = 'Ciudad no encontrada'

    
    print('\n')
    pprint(weather_data)