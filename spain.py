import requests, json

url = "https://api.covid19tracking.narrativa.com/api/countries"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))


print(data["countries"][29])