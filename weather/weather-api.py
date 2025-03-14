import requests

import os       # needed for dotenv
from   dotenv   import load_dotenv
load_dotenv()
WEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# the first draft of this is me implimenting https://medium.com/@rekalantar/how-to-build-a-simple-weather-app-in-python-with-openweathermap-api-447a2dd27898 the first hit on google just to get a hang of it

API_KEY = "" # TODO: figure out how to have secrets in repo using sops here too, and .env before that

GPS_LAT     =  42.39142595735906
GPS_LONG    = -71.12329107896443

URL = f"https://api.openweathermap.org/data/2.5/weather?lat={GPS_LAT}&lon={GPS_LONG}&appid={WEATHER_API_KEY}"

def main():
    response = requests.get(URL)
    print(f"{response}")
    if response.status_code == 200:
        data = response.json()
        # grab what you need from the blob
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
    
    else: 
        print('Error fetching weather data.')






if __name__ == '__main__':
    main()
