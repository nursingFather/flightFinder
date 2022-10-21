import requests
from flight_data import FlightData

API_KEY = "jekX2HHizaH-TA4CXPiO80sdZn583zvb"
TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com'

class FlightSearch():
    """This class is responsible for talking to the Flight Search API."""

    def get_destination_code(self, city:str):

        header = {
            "apikey":API_KEY,
        }
        parameter = {
            "term":city,
            "location_types":"city"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=parameter,headers=header)
        response.raise_for_status()
        result = response.json()["locations"]
        data = result[0]["code"]
        return data

    def cheap_flight_search(self,origin_city_code,  dest_city_code:str, from_time, to_time):
        header = {
            "apikey":API_KEY
        }
        query = {
            "fly_from":origin_city_code,
            "fly_to":dest_city_code,
            "date_from":from_time,
            "date_to": to_time,
            "night_dst_from": 7,
            "night_dst_to":30,
            "flight_type": "oneway",
            "curr":"EUR",
            "one_for_city": 1,

        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=query)
        try:
            data = response.json()['data'][0]
        except IndexError:
            print(f"No flights  found for {dest_city_code}")
            return None

        flight_data = FlightData(
            price = data["price"],
            origin_city = data["cityFrom"],
            origin_airport =  data["flyFrom"],
            destination_city =  data["cityTo"],
            destination_airport=  data["flyTo"],
            out_date =  data["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: €{flight_data.price}")
        return flight_data


