import requests, json, urllib3

urllib3.disable_warnings()
url = "https://api.covid19tracking.narrativa.com/api/countries"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))


print("Country list:")
print("----------------")

for e in data["countries"]:
    print("id =>",e["id"], "name =>",e["name"])