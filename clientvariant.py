# This is a client script each team member works collaboratively
import requests

# Variant by team_member_1: printing two quotes
for i in range(2):
    response = requests.get('http://127.0.0.1:8000/quote')
    if response.status_code == 200:
        data = response.json()
        print("Quote of the day:", data["quote"])
    else:
        print("Something went wrong. Status code:", response.status_code)