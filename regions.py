import requests, json, urllib3

def get_list_countries():
    urllib3.disable_warnings()
    url = "https://api.covid19tracking.narrativa.com/api/countries"
    response = requests.request("GET", url, verify=False)
    data = dict(json.loads(response.text))


    print("Country list:")
    print("----------------")

    for e in data["countries"]:
        print("id =>",e["id"], "name =>",e["name"])

get_list_countries()

country_id = str(input("Input country: "))

urllib3.disable_warnings()
url = "https://api.covid19tracking.narrativa.com/api/countries/"+country_id+"/regions"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))

for e in data["countries"][0][country_id]:
    print("id =>",e["id"], "name =>",e["name"])

