import requests
r = requests.get('http://api.railwayapi.com/route/train/12232/apikey/xvioc9538/')
print r.json()[0]["r"]