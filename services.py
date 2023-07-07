import requests
import json
from models import Framework


def get_frameworks():
    frameworks = []
    url = "https://e-volution.co/django784-test1a1/"

    headers = {
        'Authorization': 'Basic dXNlcjQ1OjU2ZmVkMjM1ZGY0NTNmYmM4MjZkZGMyM2QzZmRiY2FzNzNjNGZz'
    }
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        return frameworks

    data =json.loads(response.text)["data"]

    for key in data["frameworks"]:
        name = key
        market = data["frameworks"][key]
        desc = [d for d in data["desc"] if key in d]
        frameworks.append(Framework(name=name, description=desc, market=market))

    return frameworks


def get_data():
    return Framework(name="Django",
                     description="Django: Is a high-level Python web framework that encourages "
                                 "rapid development and clean",
                     market=65)
