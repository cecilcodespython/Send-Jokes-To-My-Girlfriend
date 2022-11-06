from twilio.rest import Client
from decouple import config
from my_services import create_message
import schedule 
import time
sid=config('Account_sid') # sid from twilio console
authToken=config('authToken') # authToken from twilio console

client = Client(sid,authToken)


def wAppMessage():
    body_ = create_message()

    message = client.messages.create(to=f"whatsapp:+233557362859",from_="whatsapp:+14155238886",body=body_)

    return message

schedule.every().day.at("17:45").do(wAppMessage)


while True:
    schedule.run_pending()
    time.sleep(1)