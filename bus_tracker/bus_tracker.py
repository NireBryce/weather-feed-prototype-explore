import requests

import os       # needed for dotenv
from   dotenv   import load_dotenv
load_dotenv()
TRANSIT_API_KEY = os.getenv("MBTA_V3_API_KEY")
GPS_LAT         = os.getenv("GPS_LAT")
GPS_LONG        = os.getenv("GPS_LONG")

def main():
    # Get list of stops near given location
    location = (GPS_LAT, GPS_LONG)
    radius = 0.5
    stops_url = f"https://api-v3.mbta.com/stops?latitude={location[0]}&longitude={location[1]}&radius={radius}"
    stops_response = requests.get(stops_url)
    stops_data = stops_response.json()["data"]

    # Get predictions for each stop
    predictions = []
    print(stops_data)
    for stop in stops_data:
        stop_id = stop["id"]
        predictions_url = f"https://api-v3.mbta.com/predictions?stop={stop_id}"
        predictions_response = requests.get(predictions_url)
        print(predictions_data := predictions_response.json()['data'])
        for prediction in predictions_data:
            predictions.append({
                "stop_id": stop_id,
                "route_id": prediction["relationships"]["route"]["data"]["id"],
                "direction_id": prediction["attributes"]["direction_id"],
                "arrival_time": prediction["attributes"]["arrival_time"],
                "distance": prediction["attributes"]["stop_sequence"]
            })

    # Print results
    for prediction in predictions:
        print(f"Stop {prediction['stop_id']}: Bus {prediction['route_id']} arriving at {prediction['arrival_time']} in {prediction['distance']} stops")

if __name__ == "__main__":
    main()


# def main():

#     url = "https://api-v3.mbta.com/stops"
#     params = {
#         "latitude" :    GPS_LAT,
#         "longitude":    GPS_LONG,
#         "radius"   :    0.5
#     }

#     response = requests.get(url, params=params)

#     if response.status_code == 200:
#         stops = response.json()["data"]
#         for stop in stops:
#             print(stop["attributes"]["name"])
#     else:
#         print("Failed to retrieve stops") 
