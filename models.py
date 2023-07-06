from django.db import models
from dataclasses import dataclass
import json
# Create your models here.


@dataclass
class Framework:
    name: str
    description: str
    market: int

    def __init__(self, name, description, market, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description
        self.market = market

    def to_json(self):
        return json.dumps(self.__dict__, sort_keys=False, indent=4, separators=(',', ': '))

    def save_framework(self):
        pass