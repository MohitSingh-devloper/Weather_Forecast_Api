import requests

from twilio.rest import Client

Weather_endpoint="https://api.openweathermap.org/data/2.5/onecall"
API_KEY="278bb24848a2a2fb98a40b4a4f508b76"
account_sid = "AC5707f71f7c9709a56729ab5ff02aec31"
auth_token = "c333b44c0c562d17c38deb5710442d3d"

weather_param={"lon": 79.330902,
               "lat": 30.403601,
               "appid":API_KEY,
               "exclude":"current,minutely,daily"}

response=requests.get(Weather_endpoint,params=weather_param)
response.raise_for_status()
weather_data=response.json()
weather_slice=weather_data["hourly"][:12]

will_rain=False

for hour_data in weather_slice:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's Going to Rain.Remember to bring an Umbrella.☔☔☔☔.",
        from_="+12542942493",
        to="+91 89238 94124"
    )
    print(message.status)


