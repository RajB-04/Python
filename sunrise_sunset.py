import requests

# My_lat = 75.6672326
# My_lan = 18.4632831

# parameters = {
#     "lat" : My_lat,
#     "lgn" : My_lan
# }
response = requests.get("https://api.kanye.rest")
response.raise_for_status()

data = response.json()

quote = data["quote"]
# sunset = data["sunset"]
print(data)