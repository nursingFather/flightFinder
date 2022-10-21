#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import  FlightData
from pprint import pprint
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

ORIGIN_CITY = "DUS"
date_from = datetime.today() + timedelta(days=1)
date_to = date_from + relativedelta(months=6)
SIX_MONTHS_TIME = date_to.strftime("%d/%m/%Y")
TOMORROW = date_from.strftime("%d/%m/%Y")

data_manager = DataManager()
flight_search = FlightSearch()
flight_data = FlightData()

sheet_data = data_manager.get_data()
#print(sheet_data)

for cities in sheet_data:
    if cities["iataCode"] == "":
        cities["iataCode"] = flight_search.get_destination_code(cities["city"])
        data_manager.update_sheet(iata_code=cities["iataCode"], row_id=cities["id"])
#print(sheet_data)

    flight_detail = flight_search.cheap_flight_search(origin_city_code=ORIGIN_CITY, dest_city_code=cities["iataCode"],
                                                    from_time=TOMORROW, to_time=SIX_MONTHS_TIME)

pprint(flight_detail)

