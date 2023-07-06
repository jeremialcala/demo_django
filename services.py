import requests
import json
from dataclasses import dataclass

url = "https://e-volution.co/django784-test1a1/"

headers = {
  'Authorization': 'Basic dXNlcjQ1OjU2ZmVkMjM1ZGY0NTNmYmM4MjZkZGMyM2QzZmRiY2FzNzNjNGZz'
}

response = requests.request("GET", url, headers=headers)

data =json.loads(response.text)["data"]
print(data)





@dataclass
class Framework():
    name:str
    description: str
    market: int

    def __init__(self, name, description, market):
        self.name = name
        self.description = description
        self.market = market

    def to_json(self):
        return json.dump(self)

    def save_framework(self):
        pass

frameworks = []

for key in data["frameworks"]:

    name = key
    market = data["frameworks"][key]
    desc = [d for d in data["desc"] if key in d]
    frameworks.append(Framework(name=name, description=desc, market=market))

print(frameworks)

