import requests, json, urllib3, locale
from requests.api import get

locale.setlocale(locale.LC_ALL, '')


urllib3.disable_warnings()
url = "https://api.covid19tracking.narrativa.com/api/2021-10-22/country/spain"
response = requests.request("GET", url, verify=False)
data = dict(json.loads(response.text))

spain_regions = data["dates"]["2021-10-22"]["countries"]["Spain"]["regions"]

print("Region", "New Cases", "Total cases ('%' increase)", "Deaths (24 hours)",sep="\t")

for e in range(len(spain_regions)):
    print(spain_regions[e]["name"], str(spain_regions[e]["today_new_confirmed"]), "\t"+str(spain_regions[e]["today_confirmed"]), "\t\t"+locale.format_string("%.2f", (spain_regions[e]["today_vs_yesterday_confirmed"])*100, True), spain_regions[e]["today_deaths"], sep="\t")
    
    