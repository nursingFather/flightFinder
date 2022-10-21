import requests
from pprint import pprint

sheety_endpoint = "https://api.sheety.co/ecf519ea2ca05c198bb4ca10360c1684/copyOfFlightDeals/prices"

class DataManager():

    def get_data(self):
        response = requests.get(url=sheety_endpoint)
        result = response.json()
        #print(result)
        destination_data = result["prices"]
        return destination_data

    def update_sheet(self, iata_code:str, row_id:int):

        parameter = {
            "price": {
                "iataCode": iata_code
            }
        }
        response = requests.put(url=f"{sheety_endpoint}/{row_id}", json=parameter)
        print(response.text)