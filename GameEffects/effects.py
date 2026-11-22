import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "data" / "data_effects.json"



class Effect:
    def __init__(self, entity, name_effect):
        with open(JSON_FILE, 'r', encoding="utf-8") as f:
            self.data = json.load(f)

        self.entity = entity
        self.name_effect = name_effect
        self.ageing_work = False


    #this func is using of activate effect at entity
    def using(self):
        parameters = self.data["effects"][self.name_effect]["Parameters"]
        if parameters["counter"] is None:
            return
        elif parameters["counter"] <= 0:
            match (parameters["type"]):
                case "buff":
                    self.entity.damage -= parameters["damage"]
                    self.entity.defender -= parameters["defender"]
                case "debuff":
                    self.entity.damage += parameters["damage"]
                    self.entity.defender += parameters["defender"]

            parameters["counter"] = None
            return
        else:
            if self.ageing_work:
                if parameters["type"] == "debuff" or parameters["hp"] == 0:
                    if self.entity.hp > 0:
                        self.entity.hp -= parameters["hp"]
                    else:
                        self.entity.hp = 0
                elif parameters["type"] == "healing":
                    self.entity.hp += parameters["hp"]
            else:
                match(parameters["type"]):
                    case "buff":
                        self.entity.damage += parameters["damage"]
                        self.entity.defender += parameters["defender"]
                    case "debuff":
                        self.entity.damage -= parameters["damage"]
                        self.entity.defender -= parameters["defender"]
                        if self.entity.hp > 0:
                            self.entity.hp -= parameters["hp"]
                        else:
                            self.entity.hp = 0
                    case "healing":
                        self.entity.hp += parameters["hp"]

                self.ageing_work = True

            parameters["counter"] -= 1