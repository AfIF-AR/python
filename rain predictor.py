import requests, smtplib
# import os
# from twilio.rest import Client
api_key = "d8e9d7dda3f1d98d335dd22ac314c34c"
my_email = "pybirth27@gmail.com"
password = "Pybirth@321!"
to_address = "afifbd96@gmail.com"
message = "Subject: Rain Alert\n\nHello Afif,\nBring an Umbrella Today, it might be Rain in next 12 Hours.\nHave a nice day." \
          "\n\nRegards,\nYour Python Bot"

#https://api.openweathermap.org/data/2.5/onecall?
# lat=23.810331&lon=90.412521&appid=d8e9d7dda3f1d98d335dd22ac314c34c
# Twilio App Setting-> https://www.twilio.com/docs/sms/quickstart/python
req_params = {
    "lat": 23.810331,
    "lon": 90.412521,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}
# account_sid = "AC6fbd278df7bddbeaff13193550763d6d"
# auth_token = "aa0592a9c7cbc81ed16cde2d37b65afc"


bring_umbrella = False
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=req_params)
response.raise_for_status()
weather_data = response.json()

for hour in range(12):
    if weather_data["hourly"][hour]["weather"][0]["id"] < 700:
        bring_umbrella = True
if bring_umbrella:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=message)
