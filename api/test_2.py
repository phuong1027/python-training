import requests
import json

#40VRM2wzhbpklIQRPfId4wOcwp1cx6n2w4Cpyv4P

API_KEY = "40VRM2wzhbpklIQRPfId4wOcwp1cx6n2w4Cpyv4P"
URL = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"

parameter = {
    "date": "2023-02-14"
}

response = requests.request("GET", URL, params=parameter)

data = response.json()
print(data)