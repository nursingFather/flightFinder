import requests

API_KEY = "YOUR API KEY"
TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com'
night_dst_to = 30


class FlightData:
    #This class is responsible for structuring the flight data.
    def __int__(self, price, origin_city,origin_airport, destination_city,destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date



