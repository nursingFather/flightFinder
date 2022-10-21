import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv("C:\Users\Olu\PycharmProjects\FlightFinder\.env")

account_sid = os.getenv(['TWILIO_ACCOUNT_SID'])
auth_token = os.getenv(['TWILIO_AUTH_TOKEN'])



class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    # and set the environment variables. See http://twil.io/secure

    def __init__(self):
        self.SID = account_sid
        self.TOKEN = auth_token

    def send_message(self, price:str, dep_city:str, dep_ap_iata_code: str, arr_city: str,
                     arr_ap_iata_code: str, outbound_date: str, inbound_date: str):

        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"Low price alert! only ${price} to fly from {dep_city}--{dep_ap_iata_code}"
                 f" to {arr_city}--{arr_ap_iata_code} from {outbound_date}",
            from_='+18286723422',
            status_callback='http://postb.in/1234abcd',
            to='+4915785066532'
        )

        print(message.sid)