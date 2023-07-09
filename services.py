import requests
import json
from models import Framework
from collections import OrderedDict


def get_data():
    url = "https://e-volution.co/django784-test1a1/"

    headers = {
        'Authorization': 'Basic dXNlcjQ1OjU2ZmVkMjM1ZGY0NTNmYmM4MjZkZGMyM2QzZmRiY2FzNzNjNGZz'
    }
    response = requests.request("GET", url, headers=headers)
    if response.status_code != 200:
        return {"responseCode": response.status_code, "message": "something went wrong"}

    return json.loads(response.text)["data"]


def get_frameworks():
    d = []
    # data = get_data()  #  This is the method that calls the API
    data =  \
    {
        "frameworks": {
            "Bottle": "28 %",
            "Web2Py": "55 %",
            "Flask": "35 %",
            "Django": "65 %",
            "CherryPy": "16 %"
        },
        "desc": [
            "Web2Py: Create, modify, deploy and manage application from anywhere using your browser",
            "Bottle: Is a fast, simple and lightweight WSGI micro web-framework for Python",
            "Django: Is a high-level Python web framework that encourages rapid development and clean",
            "CherryPy: Is a pythonic, object-oriented web framework",
            "Flask: provides configuration and conventions, with sensible defaults, to get started"
        ]
    }
    # Here we are ordering the data
    # TODO: save this data into a database and get some improvements on performance

    for key, value in data["frameworks"].items():
        if len(d) == 0:
            d.append({"name": key, "desc": next(d for d in data["desc"] if key in d), "market": value})
        elif int(d[-1]["market"].strip("%")) < int(value.strip("%")):
            d.insert(0, {"name": key, "desc": next(d for d in data["desc"] if key in d), "market": value})
        else:
            d.append({"name": key, "desc": next(d for d in data["desc"] if key in d), "market": value})

    return d

