import requests
url="http://127.0.0.1:8080/"
infonum={"hr":2,"period":'PM'}
r = requests.post(url,json=infonum)
print(r.json())