import requests, json, urllib3

urllib3.disable_warnings()
url = "https://api.covid19tracking.narrativa.com/api/countries/spain/regions"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))

print("Spain Regions")
print("-----------------")

sort = []
for e in data["countries"][0]["spain"]:
    sort.append(e["name"])

sort = sorted(sort)
for e in sort:
    print(e)