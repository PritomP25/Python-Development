import requests
import os
from twilio.rest import Client

OWM_Endpoint = "api.openweathermap.org/data/2.5/forecast"
api_keys = os.environ.get("") #Gain from your account
account_sid = "" #Gain from Twilio acc
auth_token = os.environ.get("") #Gain from Twilio acc


weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_keys,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
# if will_rain:
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#     .create(
#         body="It's going to rain today. Remember to bring an umbrella.",
#         from_="" #your Twilio phone number
#         to="Your verified number"
#     )
#     print(message.status)