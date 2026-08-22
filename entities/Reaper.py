from entities.Entity import Entity
from entities.save_items.inventory import Inventory
from entities.bot.Bot import Bot

class Reaper(Entity):
    def __init__(self, name = "Reaper", type_obj = "entity", hp = 150, defender = 75, damage = 25, inventory = Inventory()):
        super(Reaper, self).__init__(name, type_obj, hp, defender, damage)
        self.inventory = inventory
        self.status_action["ult"] = False
        self.bot = Bot(self)

    def auto_action(self, enemy):
        self.bot.medium_level(enemy)