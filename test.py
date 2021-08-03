import requests

url = "https://api.npoint.io/7546c56ef79d984c26f0"
response = requests.get(url)
result = response.json()
title = [item["title"]for item in result]
description = [item["description"]for item in result]
print(title)
print(description)