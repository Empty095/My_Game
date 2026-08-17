import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "data_items.json"

with open(JSON_FILE, 'r', encoding = "utf-8") as f:
    data = json.load(f)

class Item:
    def __init__(self, type_item = None, id_item = None):
        self.type_item = type_item
        self.id_item = id_item

        item_data = data["items"][self.type_item][self.id_item]

        self.name = item_data["name"]
        self.dmg = item_data["dmg"]
        self.health = item_data["health"]
        self.defender = item_data["defender"]
        self.weight = item_data["weight"]

    def bonus_dmg(self, func):
        def bonus(*args, **kwargs):
            entity_attack = func(*args, **kwargs)
            return entity_attack + self.dmg
        return bonus

    def bonus_def(self, func):
        def bonus(*args, **kwargs):
            entity_attack = func(*args, **kwargs)
            return entity_attack - self.defender
        return bonus

    def bonus_health(self, entity_hp):
        return entity_hp + self.health