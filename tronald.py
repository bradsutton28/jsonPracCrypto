import os
import requests
import json
import datetime

url="https://rickandmortyapi.com/api/character/"
response = requests.get(url)
data = response.json()

for char in data['results']:
    print(char['name'], " - ", char['species'], " - ", char['status'])










