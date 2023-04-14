import requests
import json

#40VRM2wzhbpklIQRPfId4wOcwp1cx6n2w4Cpyv4P

API_KEY = "40VRM2wzhbpklIQRPfId4wOcwp1cx6n2w4Cpyv4P"
URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

parameter = {
    "date": "2023-02-14"
}

response = requests.get(URL)  #2


data = response.json()
#print(json.dumps(data, indent=4))  #1

""" image_url = data["url"]

img_data = requests.get(image_url).content

with open ("NGC_3628.jpn", "wb") as file:
    file.writable(img_data """)

