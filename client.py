import requests

response = requests.get('http://127.0.0.1:8000/quote')
if response.status_code == 200:
    data = response.json()
    print("Quote of the day:", data["quote"])
else:
    print("Something went wrong. Status code:", response.status_code)