import requests

import os       # needed for dotenv
from   dotenv   import load_dotenv
load_dotenv()
TRANSIT_API_KEY = os.getenv("MBTA_V3_API_KEY")
GPS_LAT         = os.getenv("GPS_LAT")
GPS_LONG        = os.getenv("GPS_LONG")

def main():

    url = "https://api-v3.mbta.com/stops"
    params = {
        "latitude" :    GPS_LAT,
        "longitude":    GPS_LONG,
        "radius"   :    0.5
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        stops = response.json()["data"]
        for stop in stops:
            print(stop["attributes"]["name"])
    else:
        print("Failed to retrieve stops") 

if __name__ == "__main__":
    main()
