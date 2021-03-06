import requests, json, urllib3

api_key = "SKSormfApHlKKde7SfgeFfeWsxRSHM3e"
urllib3.disable_warnings()

location = str(input("Choose city to receive forecast from: "))

url = "http://dataservice.accuweather.com/locations/v1/cities/search?apikey="+api_key+"&q="+location+""
response = requests.request("GET", url, verify=False)
data = json.loads(response.text)
data = dict(data[0]) # response returns an ARRAY

"""
Keep getting an error about requests limit reached:

{
  "Code": "ServiceUnavailable",
  "Message": "The allowed number of requests has been exceeded.",
  "Reference": "/locations/v1/cities/search?apikey=SKSormfApHlKKde7SfgeFfeWsxRSHM3e&q=alberic"
}

Everything below are just assumptions and might not be correct. Explanation:

I get from de dictionary data the key of the city I need and save it --> city_key = data["Key"]

Once more I open a request modifying the url from the API with the city_key and I would get
from the dictionary given something to show on

SOLVED --> Only able to request 50 times a day.
UPDATED --> Modified to get temperature of the city and a simple description about the weather.
"""
city_key = data["Key"]
city_name = data["LocalizedName"]

url = "http://dataservice.accuweather.com/currentconditions/v1/"+city_key+"?apikey="+api_key+""
response = requests.request("GET", url, verify=False)
data = json.loads(response.text)
data = dict(data[0])

print("Temperature for", city_name,":", data["Temperature"]["Metric"]["Value"],"ºC")
print("Forecast:",data["WeatherText"])