import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from pprint import pprint

API_KEY = "jekX2HHizaH-TA4CXPiO80sdZn583zvb"
TEQUILA_ENDPOINT = 'https://tequila-api.kiwi.com'
night_dst_to = 30

date_from = datetime.today() + timedelta(days=1)
date_to = date_from + relativedelta(months=6)

header = {
            "apikey":API_KEY
        }
query = {
    "fly_from":"DUS",
    "fly_to":"PAR",
    "date_from":date_from.strftime("%d/%m/%Y"),
    "date_to": date_to.strftime("%d/%m/%Y"),
    "night_dst_from": 7,
    "night_dst_to":30,
    "one_for_city": 1,
    "flight_type":"oneway",
    "curr":"EUR"

}
response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=query)
#response.raise_for_status()
data = response.json()["data"][0]
pprint(data)