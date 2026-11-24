import json
from pathlib import Path

#reading file configuration data_effects.json
BASE_DIR = Path(__file__).resolve().parent
JSON_FILE = BASE_DIR / "data" / "data_effects.json"


#class effects for my game
class Effect:
    def __init__(self, entity, name_effect):
        with open(JSON_FILE, 'r', encoding="utf-8") as f:
            self.data = json.load(f)

        self.entity = entity
        self.name_effect = name_effect
        self.ageing_work = False


    #this func is using of activate effect at entity
    def using(self):
        #save effect parameters in variable
        parameters = self.data["effects"][self.name_effect]["Parameters"]

        #check effect for the presence of counter
        if parameters["counter"] is None: #if is not counter effects and execution one once
            return
        elif parameters["counter"] <= 0: #if is counter end
            match (parameters["type"]):
                case "buff":
                    self.entity.damage -= parameters["damage"]
                    self.entity.defender -= parameters["defender"]
                case "debuff":
                    self.entity.damage += parameters["damage"]
                    self.entity.defender += parameters["defender"]

            parameters["counter"] = None
            return
        else: #script job for working effects on entity
            if self.ageing_work: #if is counter on effect
                if parameters["type"] == "debuff" or parameters["hp"] == 0:
                    if self.entity.hp > 0:
                        self.entity.hp -= parameters["hp"]
                    else:
                        self.entity.hp = 0
                elif parameters["type"] == "healing":
                    self.entity.hp += parameters["hp"]
            else: #if is not used counter on effect (first start)
                match(parameters["type"]):
                    case "buff": #using at effect type "buff"
                        self.entity.damage += parameters["damage"]
                        self.entity.defender += parameters["defender"]
                    case "debuff": #using at effect type "debuff"
                        self.entity.damage -= parameters["damage"]
                        self.entity.defender -= parameters["defender"]
                        if self.entity.hp > 0:
                            self.entity.hp -= parameters["hp"]
                        else:
                            self.entity.hp = 0
                    case "healing": #using at effect type "healing"
                        self.entity.hp += parameters["hp"]

                #starting counter effect
                self.ageing_work = True

            parameters["counter"] -= 1