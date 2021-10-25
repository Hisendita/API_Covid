import requests, json, urllib3, locale
from requests.api import get

locale.setlocale(locale.LC_ALL, '')

def get_country_name():
    return spain_data["name"]

def get_confirmed():
    return locale.format_string("%d", spain_data["today_confirmed"], True)

def get_today_confirmed():
    return locale.format_string("%d", spain_data["today_new_confirmed"], True)

def get_deaths():
    return locale.format_string("%d", spain_data["today_deaths"], True)

def get_today_deaths():
    return locale.format_string("%d", spain_data["today_new_deaths"], True)

def get_global_confirmed():
    return locale.format_string("%d", global_data["today_confirmed"], True)

def get_global_today_confirmed():
    return locale.format_string("%d", global_data["today_new_confirmed"], True)

def get_global_deaths():
    return locale.format_string("%d", global_data["today_deaths"], True)

def get_global_today_deaths():
    return locale.format_string("%d", global_data["today_new_deaths"], True)
 
urllib3.disable_warnings()
url = "https://api.covid19tracking.narrativa.com/api/2021-10-22/country/spain"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))

spain_data = data["dates"]["2021-10-22"]["countries"]["Spain"]
global_data = data["total"]

print("Global Data:")
print("----------------")

print("Country", "Confirmed", "Today Confirmed", "Deaths", "Today's Deaths", sep=" // ")
print(get_country_name(),get_confirmed(),get_today_confirmed(),get_deaths(),get_today_deaths(), sep=" // ")
print("World",get_global_confirmed(),get_global_today_confirmed(),get_global_deaths(),get_global_today_deaths(), sep=" // ")